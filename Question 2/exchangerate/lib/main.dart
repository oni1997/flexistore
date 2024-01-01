import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

const String App_ID = "46d329fc45404fe4957500c747ec693b";
const String link = "https://openexchangerates.org/api/latest.json?app_id=$App_ID";

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  double? rating;

  @override
  void initState() {
    super.initState();
    Timer.periodic(Duration(seconds: 10), (Timer t) => _getExchangeRate());
  }

  Future<void> _getExchangeRate() async {
    try {
      final response = await http.get(Uri.parse(link));
      final data = json.decode(response.body);
      double zar = data["rates"]["ZAR"];
      double nok = data["rates"]["NOK"];
      setState(() {
        rating = zar / nok;
      });
      print("${_getCurrentTime()} ZAR/NOK : R ${rating!.toStringAsFixed(2)}");
    } catch (e) {
      print("Error no rates: $e");
    }
  }

  String _getCurrentTime() {
    return DateTime.now().toLocal().toString();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Exchange Rate App'),
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [Colors.white, Colors.green],
          ),
        ),
        child: Center(
          child: rating != null
              ? Text(
                  "ZAR/NOK : R ${rating!.toStringAsFixed(2)}",
                  style: TextStyle(fontSize: 24, color: Colors.black87),
                )
              : CircularProgressIndicator(),
        ),
      ),
    );
  }
}
