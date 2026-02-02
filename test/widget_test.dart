import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:chatbot_app/main.dart';
import 'package:http/http.dart' as http;

void main() {
  // Widget test for UI components
  testWidgets('Chatbot UI elements test', (WidgetTester tester) async {
    // Build ChatbotApp widget
    await tester.pumpWidget(const ChatbotApp());

    // Verify input box exists with hint text
    expect(find.byType(TextField), findsOneWidget);
    expect(
      find.widgetWithText(TextField, 'Ask your health question...'),
      findsOneWidget,
    );

    // Verify send button with send icon exists
    expect(find.byIcon(Icons.send), findsOneWidget);

    // Optional: Add more UI or interaction tests here
  });
}

// Function to test backend connectivity by sending GET request to /docs
Future<void> testBackend() async {
  try {
    final response = await http.get(Uri.parse('http://127.0.0.1:8000/docs'));
    print('Test GET status: ${response.statusCode}');
  } catch (e) {
    print('Test GET error: $e');
  }
}
