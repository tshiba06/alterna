import { defineBoot } from "@quasar/app-vite/wrappers";
import axios from "axios";

const api = axios.create({ baseURL: "http://localhost:18080" });

export default defineBoot(({ app }) => {
  app.config.globalProperties.$axios = axios;

  app.config.globalProperties.$api = api;
});

export { api, axios };
