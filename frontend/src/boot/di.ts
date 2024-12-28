import { defineBoot } from "@quasar/app-vite/wrappers";
import {
  INJECT_RAKUTEN_BANK_REPOSITORY_KEY,
  RakutenBankRepository,
} from "src/repositories/RakutenBankRepository";
import {
  INJECT_SBI_SHINSEI_BANK_REPOSITORY_KEY,
  SbiShinseiBankRepository,
} from "src/repositories/SbiShinseiBankRepository";

export default defineBoot(({ app }) => {
  app.provide(INJECT_RAKUTEN_BANK_REPOSITORY_KEY, new RakutenBankRepository());
  app.provide(INJECT_SBI_SHINSEI_BANK_REPOSITORY_KEY, new SbiShinseiBankRepository());
});
