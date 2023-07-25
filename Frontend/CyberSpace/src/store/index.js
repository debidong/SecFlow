// store/index.js
import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
        myUid: '',
        myUsername: '',
        uid: '',
        username: '',
        rid: ''
    }
  },
  mutations: {
    setRoomInfo(state, params) {
      state.myUid = params.myUid;
      state.myUsername = params.myUsername;
      state.uid = params.uid;
      state.username = params.username;
      state.rid = params.rid;
    }
  }
});

export default store;
