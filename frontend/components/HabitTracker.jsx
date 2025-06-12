
import React, { useState, useEffect } from 'react';
import HabitService from '../services/habitService';

const habitsList = ['meditation', 'hydration', 'physical'];

export default function HabitTracker() {
  const [date] = useState(new Date().toISOString().split('T')[0]);
  const [status, setStatus] = useState({});
  const [progress, setProgress] = useState({});

  useEffect(() => {
    HabitService.getStatus(date).then(res => setStatus(res.data.status));
  }, [date]);

  const toggle = (habit) => {
    const done = !status[habit];
    HabitService.addStatus(date, habit, done).then(() => {
      setStatus(prev => ({...prev, [habit]: done}));
    });
  };

  const fetchProgress = () => {
    // calculate week start (Sunday)
    const d = new Date();
    const day = d.getDay();
    d.setDate(d.getDate() - day);
    const ws = d.toISOString().split('T')[0];
    HabitService.getProgress(ws).then(res => setProgress(res.data.progress));
  };

  const completedCount = Object.values(status).filter(v=>v).length;
  const total = habitsList.length;

  return (
    <div style={{padding:20}}>
      <h2>Daily Habit Tracker</h2>
      {habitsList.map(habit=>(
        <div key={habit}>
          <label>
            <input 
              type="checkbox" 
              checked={status[habit]||false} 
              onChange={() => toggle(habit)} 
            />
            {habit}
          </label>
        </div>
      ))}
      <div style={{marginTop:10}}>
        Progress: {completedCount}/{total}
      </div>
      <button onClick={fetchProgress} style={{marginTop:10}}>
        Weekly Progress
      </button>
      {Object.keys(progress).length > 0 && (
        <pre>{JSON.stringify(progress, null, 2)}</pre>
      )}
    </div>
  );
}
