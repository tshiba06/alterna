import { type AxiosResponse } from "axios";
import { api } from "src/boot/axios";
import { inject, type InjectionKey } from "vue";

type SbiShinseiBankGetLatestResponse = {
  total: number;
};

export abstract class BaseSbiShinseiBankRepository {
  abstract getLatest(): Promise<AxiosResponse<SbiShinseiBankGetLatestResponse>>;
  abstract update(): Promise<AxiosResponse<undefined>>;
}

export class SbiShinseiBankRepository extends BaseSbiShinseiBankRepository {
  override async getLatest(): Promise<AxiosResponse<SbiShinseiBankGetLatestResponse>> {
    const res = await api.get("/banks/sbi_shinsei", {
      headers: {
        "Content-Type": "application/json",
      },
    });

    return res;
  }

  override async update(): Promise<AxiosResponse<undefined>> {
    const res = await api.post("/banks/sbi_shinsei", {
      headers: {
        "Content-Type": "application/json",
      },
    });

    return res;
  }
}

export const INJECT_SBI_SHINSEI_BANK_REPOSITORY_KEY: InjectionKey<BaseSbiShinseiBankRepository> =
  Symbol("INJECT_SBI_SHINSEI_BANK_REPOSITORY_KEY");

export const getSbiShinseiBankRepository = (): BaseSbiShinseiBankRepository => {
  const repository = inject(INJECT_SBI_SHINSEI_BANK_REPOSITORY_KEY);
  if (!repository) {
    throw new Error("no repository");
  }
  return repository;
};
