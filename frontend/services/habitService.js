
import axios from 'axios';

class HabitService {
  static addStatus(date, habit, done) {
    return axios.post('/habit', { date, habit, done });
  }
  static getStatus(date) {
    return axios.get(`/habit?date=${date}`);
  }
  static getProgress(week_start) {
    return axios.get(`/habit/progress?week_start=${week_start}`);
  }
}

export default HabitService;
