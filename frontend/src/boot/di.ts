import { defineBoot } from "@quasar/app-vite/wrappers";
import {
  INJECT_RAKUTEN_BANK_REPOSITORY_KEY,
  RakutenBankRepository,
} from "src/repositories/RakutenBankRepository";
import {
  INJECT_SBI_BENEFIT_SYSTEM_REPOSITORY_KEY,
  SbiBenefitSystemRepository,
} from "src/repositories/SbiBenefitSystemRepository";
import {
  INJECT_SBI_SHINSEI_BANK_REPOSITORY_KEY,
  SbiShinseiBankRepository,
} from "src/repositories/SbiShinseiBankRepository";
import {
  INJECT_SUMISHIN_SBI_BANK_REPOSITORY_KEY,
  SumishinSbiBankRepository,
} from "src/repositories/SumishinSbiBankRepository";

export default defineBoot(({ app }) => {
  app.provide(INJECT_RAKUTEN_BANK_REPOSITORY_KEY, new RakutenBankRepository());
  app.provide(INJECT_SBI_SHINSEI_BANK_REPOSITORY_KEY, new SbiShinseiBankRepository());
  app.provide(INJECT_SUMISHIN_SBI_BANK_REPOSITORY_KEY, new SumishinSbiBankRepository());
  app.provide(INJECT_SBI_BENEFIT_SYSTEM_REPOSITORY_KEY, new SbiBenefitSystemRepository());
});
