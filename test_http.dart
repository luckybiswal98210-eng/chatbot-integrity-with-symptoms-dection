import 'package:http/http.dart' as http;

void main() async {
  var url = Uri.parse('https://4defaf40f0e1.ngrok-free.app/docs');
  try {
    var resp = await http.get(url);
    print('Status: ${resp.statusCode}');
  } catch (e) {
    print('Failed HTTP: $e');
  }
}
