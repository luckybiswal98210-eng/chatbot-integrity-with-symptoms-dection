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
      theme: ThemeData(
        primarySwatch: Colors.teal,
        useMaterial3: true,
      ),
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
  final ScrollController _scrollController = ScrollController();

  // IMPORTANT: Update this URL after deploying to Railway/Render
  // For local development: http://127.0.0.1:8000
  // For production: https://your-app-name.railway.app or your deployed URL
  final String apiBaseUrl = "https://web-production-c2ec2.up.railway.app";

  List<Map<String, dynamic>> messages = [];
  String sessionId = DateTime.now().millisecondsSinceEpoch.toString();
  bool isLoading = false;

  final List<Map<String, String>> languages = [
    {"code": "en", "label": "English"},
    {"code": "hi", "label": "Hindi"},
    {"code": "ta", "label": "Tamil"},
    {"code": "te", "label": "Telugu"},
    {"code": "kn", "label": "Kannada"},
  ];

  String selectedLanguage = "en";

  @override
  void initState() {
    super.initState();
    // Add welcome message
    WidgetsBinding.instance.addPostFrameCallback((_) {
      setState(() {
        messages.add({
          "sender": "bot",
          "text": "Welcome to AROGYA VANI! 🏥\n\nI'm here to help with your health concerns. Please describe your main symptom, and I'll ask you a few questions to provide personalized advice.",
        });
      });
    });
  }

  Future<void> sendMessage(String text) async {
    if (text.trim().isEmpty) return;

    setState(() {
      messages.add({"sender": "user", "text": text});
      isLoading = true;
    });

    _scrollToBottom();

    try {
      final response = await http.post(
        Uri.parse('$apiBaseUrl/chat'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          "question": text,
          "language": selectedLanguage,
          "session_id": sessionId,
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          messages.add({
            "sender": "bot",
            "text": data["response_text"],
            "audio": data["audio_url"],
          });
          isLoading = false;
        });
        _scrollToBottom();
      } else {
        setState(() {
          messages.add({
            "sender": "bot",
            "text": "Error contacting server. Please try again."
          });
          isLoading = false;
        });
      }
    } catch (e) {
      setState(() {
        messages.add({
          "sender": "bot",
          "text": "Failed to connect to server. Please check if the backend is running."
        });
        isLoading = false;
      });
    }
  }

  Future<void> resetConversation() async {
    try {
      await http.post(
        Uri.parse('$apiBaseUrl/reset'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({"session_id": sessionId}),
      );

      setState(() {
        sessionId = DateTime.now().millisecondsSinceEpoch.toString();
        messages.clear();
        messages.add({
          "sender": "bot",
          "text": "Conversation reset. How can I help you today?",
        });
      });
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Failed to reset conversation")),
      );
    }
  }

  void _scrollToBottom() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          _scrollController.position.maxScrollExtent,
          duration: const Duration(milliseconds: 300),
          curve: Curves.easeOut,
        );
      }
    });
  }

  Widget buildMessage(Map<String, dynamic> msg) {
    final bool isUser = msg["sender"] == "user";
    final String text = msg["text"] ?? "";
    final String audio = msg["audio"] ?? "";

    return Container(
      alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: Column(
        crossAxisAlignment:
            isUser ? CrossAxisAlignment.end : CrossAxisAlignment.start,
        children: [
          Container(
            constraints: BoxConstraints(
              maxWidth: MediaQuery.of(context).size.width * 0.75,
            ),
            decoration: BoxDecoration(
              color: isUser
                  ? Colors.teal.shade600
                  : Colors.grey.shade200,
              borderRadius: BorderRadius.circular(16),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withOpacity(0.1),
                  blurRadius: 4,
                  offset: const Offset(0, 2),
                ),
              ],
            ),
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            child: Text(
              text,
              style: TextStyle(
                color: isUser ? Colors.white : Colors.black87,
                fontSize: 15,
              ),
            ),
          ),

          // 🔊 PLAY BUTTON (WEB SAFE)
          if (!isUser && audio.isNotEmpty && kIsWeb)
            Padding(
              padding: const EdgeInsets.only(top: 4),
              child: TextButton.icon(
                icon: const Icon(Icons.volume_up, size: 18),
                label: const Text("Play audio"),
                style: TextButton.styleFrom(
                  foregroundColor: Colors.teal,
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                ),
                onPressed: () {
                  final player = html.AudioElement()
                    ..src = "$apiBaseUrl$audio"
                    ..controls = true;
                  player.play();
                },
              ),
            ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "AROGYA VANI",
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        backgroundColor: Colors.teal.shade700,
        foregroundColor: Colors.white,
        elevation: 2,
        actions: [
          // Language selector
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8),
            child: DropdownButton<String>(
              value: selectedLanguage,
              underline: Container(),
              dropdownColor: Colors.teal.shade700,
              style: const TextStyle(color: Colors.white),
              icon: const Icon(Icons.language, color: Colors.white),
              onChanged: (v) {
                if (v != null) setState(() => selectedLanguage = v);
              },
              items: languages
                  .map(
                    (l) => DropdownMenuItem(
                      value: l["code"],
                      child: Text(
                        l["label"]!,
                        style: const TextStyle(color: Colors.white),
                      ),
                    ),
                  )
                  .toList(),
            ),
          ),
          // Reset button
          IconButton(
            icon: const Icon(Icons.refresh),
            tooltip: "Reset Conversation",
            onPressed: resetConversation,
          ),
        ],
      ),
      body: Column(
        children: [
          // Messages list
          Expanded(
            child: messages.isEmpty
                ? const Center(
                    child: CircularProgressIndicator(),
                  )
                : ListView.builder(
                    controller: _scrollController,
                    itemCount: messages.length,
                    itemBuilder: (_, i) => buildMessage(messages[i]),
                  ),
          ),

          // Loading indicator
          if (isLoading)
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Row(
                children: [
                  const SizedBox(width: 16),
                  SizedBox(
                    width: 20,
                    height: 20,
                    child: CircularProgressIndicator(
                      strokeWidth: 2,
                      color: Colors.teal.shade600,
                    ),
                  ),
                  const SizedBox(width: 12),
                  Text(
                    "Thinking...",
                    style: TextStyle(
                      color: Colors.grey.shade600,
                      fontStyle: FontStyle.italic,
                    ),
                  ),
                ],
              ),
            ),

          // Input area
          Container(
            decoration: BoxDecoration(
              color: Colors.white,
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withOpacity(0.1),
                  blurRadius: 4,
                  offset: const Offset(0, -2),
                ),
              ],
            ),
            padding: const EdgeInsets.all(12),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    enabled: !isLoading,
                    onSubmitted: (t) {
                      if (!isLoading) {
                        sendMessage(t);
                        _controller.clear();
                      }
                    },
                    decoration: InputDecoration(
                      hintText: "Type your message...",
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(24),
                        borderSide: BorderSide(color: Colors.teal.shade300),
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(24),
                        borderSide: BorderSide(color: Colors.teal.shade600, width: 2),
                      ),
                      contentPadding: const EdgeInsets.symmetric(
                        horizontal: 20,
                        vertical: 12,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                Container(
                  decoration: BoxDecoration(
                    color: Colors.teal.shade600,
                    shape: BoxShape.circle,
                  ),
                  child: IconButton(
                    icon: const Icon(Icons.send, color: Colors.white),
                    onPressed: isLoading
                        ? null
                        : () {
                            sendMessage(_controller.text);
                            _controller.clear();
                          },
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
