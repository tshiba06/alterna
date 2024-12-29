import { type AxiosResponse } from "axios";
import { api } from "src/boot/axios";
import { inject, type InjectionKey } from "vue";

type SumishinSbiBankGetLatestResponse = {
  total: number;
};

export abstract class BaseSumishinSbiBankRepository {
  abstract getLatest(): Promise<AxiosResponse<SumishinSbiBankGetLatestResponse>>;
  abstract update(): Promise<AxiosResponse<undefined>>;
}

export class SumishinSbiBankRepository extends BaseSumishinSbiBankRepository {
  override async getLatest(): Promise<AxiosResponse<SumishinSbiBankGetLatestResponse>> {
    const res = await api.get("/banks/sumishin_sbi", {
      headers: {
        "Content-Type": "application/json",
      },
    });

    return res;
  }

  override async update(): Promise<AxiosResponse<undefined>> {
    const res = await api.post("/banks/sumishin_sbi", {
      headers: {
        "Content-Type": "application/json",
      },
    });

    return res;
  }
}

export const INJECT_SUMISHIN_SBI_BANK_REPOSITORY_KEY: InjectionKey<BaseSumishinSbiBankRepository> =
  Symbol("INJECT_SUMISHIN_SBI_BANK_REPOSITORY_KEY");

export const getSumishinSbiBankRepository = (): BaseSumishinSbiBankRepository => {
  const repository = inject(INJECT_SUMISHIN_SBI_BANK_REPOSITORY_KEY);
  if (!repository) {
    throw new Error("no repository");
  }
  return repository;
};
