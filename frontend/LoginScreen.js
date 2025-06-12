import React, { useState } from 'react';
import { View, TextInput, Button, StyleSheet, Alert } from 'react-native';
import auth from '@react-native-firebase/auth';

const LoginScreen = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    auth()
      .signInWithEmailAndPassword(email, password)
      .then(() => Alert.alert('Login Successful'))
      .catch(error => Alert.alert('Login Failed', error.message));
  };

  const handleRegister = () => {
    auth()
      .createUserWithEmailAndPassword(email, password)
      .then(() => Alert.alert('Account Created'))
      .catch(error => Alert.alert('Registration Failed', error.message));
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Email"
        onChangeText={setEmail}
        value={email}
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        onChangeText={setPassword}
        value={password}
        secureTextEntry
      />
      <Button title="Login" onPress={handleLogin} />
      <Button title="Register" onPress={handleRegister} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1, justifyContent: 'center', padding: 16,
  },
  input: {
    height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 12, paddingHorizontal: 8,
  },
});

export default LoginScreen;