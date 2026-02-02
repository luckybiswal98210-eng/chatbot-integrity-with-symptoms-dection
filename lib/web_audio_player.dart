import 'dart:html' as html;
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

class WebAudioPlayer extends StatelessWidget {
  final String audioUrl;

  const WebAudioPlayer({super.key, required this.audioUrl});

  @override
  Widget build(BuildContext context) {
    if (!kIsWeb) {
      return const SizedBox();
    }

    final player = html.AudioElement()
      ..src = audioUrl
      ..controls = true;

    return SizedBox(height: 40, child: HtmlElementView(viewType: audioUrl));
  }
}
