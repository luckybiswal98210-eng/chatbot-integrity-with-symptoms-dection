import 'dart:convert';
import 'dart:html' as html;
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const ChatbotApp());
}

class ChatbotApp extends StatelessWidget {
  const ChatbotApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AROGYA VANI',
      debugShowCheckedModeBanner: false,
      home: const ChatbotPage(),
    );
  }
}

class ChatbotPage extends StatefulWidget {
  const ChatbotPage({super.key});

  @override
  State<ChatbotPage> createState() => _ChatbotPageState();
}

class _ChatbotPageState extends State<ChatbotPage> {
  final TextEditingController _controller = TextEditingController();

  final String apiBaseUrl = "http://127.0.0.1:8000";

  List<Map<String, dynamic>> messages = [];

  final List<Map<String, String>> languages = [
    {"code": "en", "label": "English"},
    {"code": "hi", "label": "Hindi"},
    {"code": "ta", "label": "Tamil"},
    {"code": "te", "label": "Telugu"},
    {"code": "kn", "label": "Kannada"},
  ];

  String selectedLanguage = "en";

  Future<void> sendMessage(String text) async {
    if (text.trim().isEmpty) return;

    setState(() {
      messages.add({"sender": "user", "text": text});
    });

    try {
      final response = await http.post(
        Uri.parse('$apiBaseUrl/chat'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({"question": text, "language": selectedLanguage}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          messages.add({
            "sender": "bot",
            "text": data["response_text"],
            "audio": data["audio_url"],
          });
        });
      } else {
        setState(() {
          messages.add({"sender": "bot", "text": "Error contacting server"});
        });
      }
    } catch (e) {
      setState(() {
        messages.add({"sender": "bot", "text": "Failed to connect to API"});
      });
    }
  }

  Widget buildMessage(Map<String, dynamic> msg) {
    final bool isUser = msg["sender"] == "user";
    final String text = msg["text"] ?? "";
    final String audio = msg["audio"] ?? "";

    return Container(
      alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
      padding: const EdgeInsets.all(8),
      child: Column(
        crossAxisAlignment: isUser
            ? CrossAxisAlignment.end
            : CrossAxisAlignment.start,
        children: [
          Container(
            decoration: BoxDecoration(
              color: isUser ? Colors.blueAccent : Colors.grey.shade300,
              borderRadius: BorderRadius.circular(12),
            ),
            padding: const EdgeInsets.all(12),
            child: Text(
              text,
              style: TextStyle(color: isUser ? Colors.white : Colors.black),
            ),
          ),

          // 🔊 PLAY BUTTON (WEB SAFE)
          if (!isUser && audio.isNotEmpty && kIsWeb)
            TextButton.icon(
              icon: const Icon(Icons.play_arrow),
              label: const Text("Play audio"),
              onPressed: () {
                final player = html.AudioElement()
                  ..src = "$apiBaseUrl$audio"
                  ..controls = true;
                player.play();
              },
            ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("AROGYA VANI"),
        actions: [
          DropdownButton<String>(
            value: selectedLanguage,
            underline: Container(),
            onChanged: (v) {
              if (v != null) setState(() => selectedLanguage = v);
            },
            items: languages
                .map(
                  (l) => DropdownMenuItem(
                    value: l["code"],
                    child: Text(l["label"]!),
                  ),
                )
                .toList(),
          ),
        ],
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (_, i) => buildMessage(messages[i]),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    onSubmitted: (t) {
                      sendMessage(t);
                      _controller.clear();
                    },
                    decoration: const InputDecoration(
                      hintText: "Ask your health question…",
                      border: OutlineInputBorder(),
                    ),
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.send),
                  onPressed: () {
                    sendMessage(_controller.text);
                    _controller.clear();
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
