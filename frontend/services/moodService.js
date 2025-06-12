import axios from 'axios';

class MoodService {
  static async saveMood(date, mood, note) {
    const response = await axios.post('/mood', { date, mood, note });
    return response.data;
  }
  static async getMood(date) {
    const response = await axios.get('/mood', { params: { date } });
    return response.data;
  }
}

export default MoodService;
