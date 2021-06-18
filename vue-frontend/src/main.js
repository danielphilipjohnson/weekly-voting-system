import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "./assets/tailwind.css";
import "./registerServiceWorker";

import axios from "axios";

axios.defaults.baseURL = "http://0.0.0.0:8088/";

createApp(App).use(store).use(router).mount("#app");
