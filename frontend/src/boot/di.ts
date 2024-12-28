import { defineBoot } from "@quasar/app-vite/wrappers";
import {
  INJECT_RAKUTEN_BANK_REPOSITORY_KEY,
  RakutenBankRepository,
} from "src/repository/RakutenBankRepository";

export default defineBoot(({ app }) => {
  app.provide(INJECT_RAKUTEN_BANK_REPOSITORY_KEY, new RakutenBankRepository());
});
