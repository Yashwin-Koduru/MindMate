import axios from 'axios';

class CoachService {
  async getReply(history) {
    const resp = await axios.post('/coach', { history });
    return resp.data.reply;
  }
}

export default new CoachService();
