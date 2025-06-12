import React, { useState } from 'react';
import MoodService from '../services/moodService';

const emojis = ['😢','😞','😐','😊','😃'];

export default function MoodTracker() {
  const [mood, setMood] = useState(2);
  const [note, setNote] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const date = new Date().toISOString().split('T')[0];
    try {
      await MoodService.saveMood(date, mood, note);
      setStatus('Saved!');
    } catch {
      setStatus('Error saving mood.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4">
      <h2 className="text-xl mb-2">Daily Mood Tracking</h2>
      <div className="flex items-center">
        <span className="text-3xl mr-2">{emojis[mood]}</span>
        <input
          type="range"
          min="0"
          max="4"
          value={mood}
          onChange={e => setMood(Number(e.target.value))}
          className="flex-1"
        />
      </div>
      <textarea
        placeholder="Optional notes"
        value={note}
        onChange={e => setNote(e.target.value)}
        className="w-full h-20 mt-2 p-1 border rounded"
      />
      <button type="submit" className="mt-2 px-4 py-2 rounded shadow bg-blue-500 text-white">
        Submit
      </button>
      {status && <p className="mt-2">{status}</p>}
    </form>
