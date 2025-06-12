import React, { useState } from 'react';
import coachService from '../services/coachService';

export default function ChatCoach() {
  const [messages, setMessages] = useState([
    { role: 'system', content: 'You are a helpful mental health coach.' }
  ]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (!input) return;
    const newMessage = { role: 'user', content: input };
    const newHistory = [...messages, newMessage];
    setMessages(newHistory);
    setInput('');
    const reply = await coachService.getReply(newHistory);
    setMessages([...newHistory, { role: 'assistant', content: reply }]);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Mental Health Coach</h2>
      <div style={{ maxHeight: 300, overflowY: 'scroll', border: '1px solid #ccc', padding: 10 }}>
        {messages.map((m, i) => (
          <div key={i} style={{ textAlign: m.role === 'user' ? 'right' : 'left' }}>
            <strong>{m.role}:</strong> {m.content}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        style={{ width: '80%', marginRight: 10 }}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}
