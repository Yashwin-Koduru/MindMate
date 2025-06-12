import React, { useEffect, useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Picker, Alert, ScrollView } from 'react-native';

const JournalScreen = () => {
  const [templates, setTemplates] = useState({});
  const [selectedTemplate, setSelectedTemplate] = useState('');
  const [entryText, setEntryText] = useState('');
  const [userId, setUserId] = useState('test_user'); // Replace with actual user ID from auth

  useEffect(() => {
    fetch('http://localhost:5000/journal/templates')
      .then((res) => res.json())
      .then((data) => setTemplates(data))
      .catch((err) => Alert.alert('Error', 'Could not load templates'));
  }, []);

  const handleSubmit = () => {
    if (!selectedTemplate || !entryText) {
      Alert.alert('Missing Info', 'Please select a prompt and write an entry.');
      return;
    }

    fetch('http://localhost:5000/journal/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: userId,
        template_type: selectedTemplate,
        entry: entryText,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.status === 'success') {
          Alert.alert('Saved', 'Your journal entry was saved.');
          setEntryText('');
        } else {
          Alert.alert('Error', data.message);
        }
      })
      .catch((err) => Alert.alert('Error', 'Submission failed.'));
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Guided Journaling</Text>
      <Picker
        selectedValue={selectedTemplate}
        onValueChange={(itemValue) => setSelectedTemplate(itemValue)}
        style={styles.picker}
      >
        <Picker.Item label="Select a prompt..." value="" />
        {Object.keys(templates).map((key) => (
          <Picker.Item key={key} label={templates[key]} value={key} />
        ))}
      </Picker>
      <TextInput
        style={styles.input}
        multiline
        placeholder="Write your thoughts here..."
        value={entryText}
        onChangeText={setEntryText}
      />
      <Button title="Submit Entry" onPress={handleSubmit} />
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flexGrow: 1, justifyContent: 'center', padding: 20 },
  title: { fontSize: 24, marginBottom: 20, textAlign: 'center' },
  picker: { marginBottom: 20 },
  input: {
    height: 150,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 20,
    paddingHorizontal: 10,
    paddingVertical: 10,
    textAlignVertical: 'top',
  },
});

export default JournalScreen;