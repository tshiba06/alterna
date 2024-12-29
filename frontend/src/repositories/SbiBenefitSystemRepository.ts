import type { AxiosResponse } from "axios";
import { api } from "src/boot/axios";
import { inject, type InjectionKey } from "vue";

type SbiBenefitSystemGetLatestResponse = {
  total: number;
};

export abstract class BaseSbiBenefitSystemRepository {
  abstract getLatest(): Promise<AxiosResponse<SbiBenefitSystemGetLatestResponse>>;
  abstract update(): Promise<AxiosResponse<undefined>>;
}

export class SbiBenefitSystemRepository extends BaseSbiBenefitSystemRepository {
  override async getLatest(): Promise<AxiosResponse<SbiBenefitSystemGetLatestResponse>> {
    const res = await api.get("/pensions/sbi_benefit_system", {
      headers: {
        "Content-Type": "application/json",
      },
    });

    return res;
  }

  override async update(): Promise<AxiosResponse<undefined>> {
    const res = await api.post("/pensions/sbi_benefit_system", {
      headers: {
        "Content-Type": "application/json",
      },
    });

    return res;
  }
}

export const INJECT_SBI_BENEFIT_SYSTEM_REPOSITORY_KEY: InjectionKey<BaseSbiBenefitSystemRepository> =
  Symbol("INJECT_SBI_BENEFIT_SYSTEM_REPOSITORY_KEY");

export const getSbiBenefitSystemRepository = (): BaseSbiBenefitSystemRepository => {
  const repository = inject(INJECT_SBI_BENEFIT_SYSTEM_REPOSITORY_KEY);
  if (!repository) {
    throw new Error("no repository");
  }
  return repository;
};
