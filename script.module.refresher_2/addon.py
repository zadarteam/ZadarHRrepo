# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHhibWMsIHhibWNhZGRvbiwgeGJtY2d1aSwgeGJtY3Zmcw0KZnJvbSByZXNvdXJjZXMubGliIGltcG9ydCBzaW1wbGVqc29uIGFzIGpzb24NCmZyb20gcmVzb3VyY2VzLmxpYiBpbXBvcnQgcmVxdWVzdHMNCmltcG9ydCB1dWlkDQppbXBvcnQgb3MNCmltcG9ydCB4bWwuZXRyZWUuRWxlbWVudFRyZWUgYXMgRVQNCmxpbnV4ID0gRmFsc2UNClByb2dyZXNzRGlhbG9nID0geGJtY2d1aS5EaWFsb2dQcm9ncmVzcygpDQpJbmZvRGlhbG9nID0geGJtY2d1aS5EaWFsb2coKQ0KUHJvZ3Jlc3NEaWFsb2cuY3JlYXRlKCdWSFMgUFZSIENoYW5nZXInLCAnJykNClByb2dyZXNzRGlhbG9nLnVwZGF0ZSgwLCAnUG9rcmXEh2VtJykNCg0KZGVmIGRlZmluZV9wdnJfbG9jYXRpb24oKToNCiAgICB0cnk6DQogICAgICAgIF9fYWRkb25fXyA9IHhibWNhZGRvbi5BZGRvbihpZD0ncHZyLnphZGFydGVhbXc2NG1hdCcpDQogICAgZXhjZXB0Og0KICAgICAgICBwYXNzDQogICAgdHJ5Og0KICAgICAgICBfX2FkZG9uX18gPSB4Ym1jYWRkb24uQWRkb24oaWQ9J3B2ci56YWRhcnRlYW1hYXJjaDY0bWF0JykNCiAgICBleGNlcHQ6DQogICAgICAgIHBhc3MNCiAgICB0cnk6DQogICAgICAgIF9fYWRkb25fXyA9IHhibWNhZGRvbi5BZGRvbihpZD0ncHZyLnphZGFydGVhbWFybXY3bWF0JykNCiAgICBleGNlcHQ6DQogICAgICAgIHBhc3MNCiAgICB0cnk6DQogICAgICAgIF9fYWRkb25fXyA9IHhibWNhZGRvbi5BZGRvbihpZD0ncHZyLnphZGFydGVhbXdpNjg2bWF0JykNCiAgICBleGNlcHQ6DQogICAgICAgIHBhc3MNCiAgICB0cnk6DQogICAgICAgIF9fYWRkb25fXyA9IHhibWNhZGRvbi5BZGRvbihpZD0ncHZyLnN0YWxrZXInKQ0KICAgIGV4Y2VwdDoNCiAgICAgICAgcGFzcw0KICAgIGVsc2U6DQogICAgICAgIGxpbnV4ID0gVHJ1ZQ0KICAgIF9fYWRkb25kaXJfXyA9IHhibWN2ZnMudHJhbnNsYXRlUGF0aCggX19hZGRvbl9fLmdldEFkZG9uSW5mbygncHJvZmlsZScpICkNCiAgICBwYXRoID0gb3MucGF0aC5qb2luKF9fYWRkb25kaXJfXywgJ3NldHRpbmdzLnhtbCcpDQogICAgcmV0dXJuIHBhdGgNCg0KZGVmIGdldF9saWNlbmNlX2Zyb21fY2xpZW50KHZhbGlkPVRydWUpOg0KICAgIGlmIHZhbGlkOg0KICAgICAgICBsaWNlbmNlID0gJycNCiAgICAgICAgcGFyc2VyID0gRVQuWE1MUGFyc2VyKGVuY29kaW5nPSJ1dGYtOCIpDQogICAgICAgIGFkZG9uID0geGJtY2FkZG9uLkFkZG9uKGlkPSdzY3JpcHQubW9kdWxlLnJlZnJlc2hlcicpDQogICAgICAgIGRpciA9IHhibWN2ZnMudHJhbnNsYXRlUGF0aChhZGRvbi5nZXRBZGRvbkluZm8oJ3Byb2ZpbGUnKSkNCiAgICAgICAgdHJ5Og0KICAgICAgICAgICAgcGF0aCA9IG9zLnBhdGguam9pbihkaXIsICdzZXR0aW5ncy54bWwnKQ0KICAgICAgICAgICAgdHJlZSA9IEVULnBhcnNlKHBhdGgsIHBhcnNlcj1wYXJzZXIpDQogICAgICAgICAgICByb290ID0gdHJlZS5nZXRyb290KCkNCiAgICAgICAgICAgIGZvciBpZCBpbiByb290Og0KICAgICAgICAgICAgICAgIGlmIGlkLmF0dHJpYlsnaWQnXSA9PSAnbGljZW5jZV9rZXknOg0KICAgICAgICAgICAgICAgICAgICBsaWNlbmNlID0gaWQudGV4dA0KICAgICAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6DQogICAgICAgICAgICBsaWNlbmNlID0gJycNCiAgICAgICAgZmluYWxseToNCiAgICAgICAgICAgIHJldHVybiBsaWNlbmNlDQoNCmRlZiBnZXRfYWRkb25faWQoKToNCiAgICBsaWNlbmNlID0gJycNCiAgICBwYXJzZXIgPSBFVC5YTUxQYXJzZXIoZW5jb2Rpbmc9InV0Zi04IikNCiAgICBhZGRvbiA9IHhibWNhZGRvbi5BZGRvbihpZD0nc2NyaXB0Lm1vZHVsZS5yZWZyZXNoZXInKQ0KICAgIGRpciA9IHhibWN2ZnMudHJhbnNsYXRlUGF0aChhZGRvbi5nZXRBZGRvbkluZm8oJ3Byb2ZpbGUnKSkNCiAgICB0cnk6DQogICAgICAgIHBhdGggPSBvcy5wYXRoLmpvaW4oZGlyLCAnc2V0dGluZ3MueG1sJykNCiAgICAgICAgdHJlZSA9IEVULnBhcnNlKHBhdGgsIHBhcnNlcj1wYXJzZXIpDQogICAgICAgIHJvb3QgPSB0cmVlLmdldHJvb3QoKQ0KICAgICAgICBmb3IgaWQgaW4gcm9vdDoNCiAgICAgICAgICAgIGlmIGlkLmF0dHJpYlsnaWQnXSA9PSAnY2xpZW50X2tleSc6DQogICAgICAgICAgICAgICAgbGljZW5jZSA9IGlkLnRleHQNCiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6DQogICAgICAgIGxpY2VuY2UgPSAnJw0KICAgIGZpbmFsbHk6DQogICAgICAgIHJldHVybiBsaWNlbmNlDQoNCg0KDQoNCiNCQVNFX1VSTCA9ICdodH'
love = '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'
god = 'Zy5hdHRyaWJbJ2lkJ10gPT0gJ3NlcnZlcl8wJzoNCiAgICAgICAgICBzZXR0aW5nLnRleHQgPSBzZXJ2ZXINCiAgICBuZXdfeG1sID0gRVQudG9zdHJpbmcocm9vdCwgZW5jb2Rpbmc9J3V0Zi04JykNCiAgICBmID0geGJtY3Zmcy5GaWxlKHBhdGgsICd3YicpDQogICAgZi53cml0ZShuZXdfeG1sKQ0KICAgIGYuY2xvc2UoKQ0KDQpkZWYgZGlzYWJsZV9wdnIoKToNCiAgeGJtYy5leGVjdXRlSlNPTlJQQygneyJqc29ucnBjIjoiMi4wIiwibWV0aG9kIjoiQWRkb25zLlNldEFkZG9uRW5hYmxlZCIsImlkIjo3LCJwYXJhbXMiOnsiYWRkb25pZCI6ICJwdnIuemFkYXJ0ZWFtdzY0bWF0IiwiZW5hYmxlZCI6ZmFsc2V9fScpDQogIHhibWMuZXhlY3V0ZUpTT05SUEMoJ3sianNvbnJwYyI6IjIuMCIsIm1ldGhvZCI6IkFkZG9ucy5TZXRBZGRvbkVuYWJsZWQiLCJpZCI6NywicGFyYW1zIjp7ImFkZG9uaWQiOiAicHZyLnphZGFydGVhbWFhcmNoNjRtYXQiLCJlbmFibGVkIjpmYWxzZX19JykNCiAgeGJtYy5leGVjdXRlSlNPTlJQQygneyJqc29ucnBjIjoiMi4wIiwibWV0aG9kIjoiQWRkb25zLlNldEFkZG9uRW5hYmxlZCIsImlkIjo3LCJwYXJhbXMiOnsiYWRkb25pZCI6ICJwdnIuemFkYXJ0ZWFtYXJtdjdtYXQiLCJlbmFibGVkIjpmYWxzZX19JykNCiAgeGJtYy5leGVjdXRlSlNPTlJQQygneyJqc29ucnBjIjoiMi4wIiwibWV0aG9kIjoiQWRkb25zLlNldEFkZG9uRW5hYmxlZCIsImlkIjo3LCJwYXJhbXMiOnsiYWRkb25pZCI6ICJwdnIuemFkYXJ0ZWFtd2k2ODZtYXQiLCJlbmFibGVkIjpmYWxzZX19JykNCiAgeGJtYy5leGVjdXRlSlNPTlJQQygneyJqc29ucnBjIjoiMi4wIiwibWV0aG9kIjoiQWRkb25zLlNldEFkZG9uRW5hYmxlZCIsImlkIjo3LCJwYXJhbXMiOnsiYWRkb25pZCI6ICJwdnIuc3RhbGtlciIsImVuYWJsZWQiOmZhbHNlfX0nKQ0KDQpkZWYgZW5hYmxlX3B2cigpOg0KICB4Ym1jLmV4ZWN1dGVKU09OUlBDKCd7Impzb25ycGMiOiIyLjAiLCJtZXRob2QiOiJBZGRvbnMuU2V0QWRkb25FbmFibGVkIiwiaWQiOjcsInBhcmFtcyI6eyJhZGRvbmlkIjogInB2ci56YWRhcnRlYW13NjRtYXQiLCJlbmFibGVkIjp0cnVlfX0nKQ0KICB4Ym1jLmV4ZWN1dGVKU09OUlBDKCd7Impzb25ycGMiOiIyLjAiLCJtZXRob2QiOiJBZGRvbnMuU2V0QWRkb25FbmFibGVkIiwiaWQiOjcsInBhcmFtcyI6eyJhZGRvbmlkIjogInB2ci56YWRhcnRlYW1hYXJjaDY0bWF0IiwiZW5hYmxlZCI6dHJ1ZX19JykNCiAgeGJtYy5leGVjdXRlSlNPTlJQQygneyJqc29ucnBjIjoiMi4wIiwibWV0aG9kIjoiQWRkb25zLlNldEFkZG9uRW5hYmxlZCIsImlkIjo3LCJwYXJhbXMiOnsiYWRkb25pZCI6ICJwdnIuemFkYXJ0ZWFtYXJtdjdtYXQiLCJlbmFibGVkIjp0cnVlfX0nKQ0KICB4Ym1jLmV4ZWN1dGVKU09OUlBDKCd7Impzb25ycGMiOiIyLjAiLCJtZXRob2QiOiJBZGRvbnMuU2V0QWRkb25FbmFibGVkIiwiaWQiOjcsInBhcmFtcyI6eyJhZGRvbmlkIjogInB2ci56YWRhcnRlYW13aTY4Nm1hdCIsImVuYWJsZWQiOnRydWV9fScpDQogIHhibWMuZXhlY3V0ZUpTT05SUEMoJ3sianNvbnJwYyI6IjIuMCIsIm1ldGhvZCI6IkFkZG9ucy5TZXRBZGRvbkVuYWJsZWQiLCJpZCI6NywicGFyYW1zIjp7ImFkZG9uaWQiOiAicHZyLnN0YWxrZXIiLCJlbmFibGVkIjp0cnVlfX0nKQ0KDQoNCmRlZiBzdGFydCgpOg0KICAgIFByb2dyZXNzRGlhbG9nLnVwZGF0ZSgxMCwgJ1RyYcW+aW0gSUQnKQ0KICAgIHVzZXJfaWQgPSBnZXRfdXNlcl9pZCgpDQogICAgUHJvZ3Jlc3NEaWFsb2cudXBkYXRlKDIwLCAnVHJhxb5pbSBsaWNlbmN1JykNCiAgICBsaWNlbmNlID0gZ2V0X2xpY2VuY2VfZnJvbV9jbGllbnQoKQ0KICAgIGNsaWVudF9pZCA9IGdldF9hZGRvbl9pZCgpDQogICAgUHJvZ3Jlc3NEaWFsb2cudXBkYXRlKDMwLCAnUHJvdmplcmF2YW0gbGljZW5jdScpDQogICAgbGlzdF9udW0gPSBJbmZvRGlhbG9nLm51bWVyaWMoMCwgJ09kYWJlcml0ZSBicm9qIGxpc3RlJykNCiAgICBsaXN0X251bWJlciA9IGludChsaXN0X251bSkNCiAgICByZXNwb25zZSA9IGdldF9uZXdfbGlzdChsaXN0X251bWJlciwgbGljZW5jZSwgY2xpZW50X2lkLCB1c2VyX2lkKQ0KICAgIGlmIHJlc3BvbnNlWydtb2RlJ11bJ3N0YXR1cyddID09ICdFcnJvcic6DQogICAgICAgIG1lc3NhZ2UgPSByZXNwb25zZVsnbW9kZSddWydkYXRhJ10NCiAgICAgICAgaWYgbWVzc2FnZSA9PSAnVXBkYXRlS29kaSc6DQogICAgICAgICAgICBJbmZvRGlhbG9nLm9rKCdWSFMgUFZSIENoYW5nZXInLCAnUE'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))