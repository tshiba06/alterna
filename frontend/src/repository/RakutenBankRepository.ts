import type { AxiosResponse } from "axios";
import { api } from "src/boot/axios";
import { inject, type InjectionKey } from "vue";

type RakutenBankGetLatestResponse = {
  total: number;
};

export abstract class BaseRakutenBankRepository {
  abstract getLatest(): Promise<AxiosResponse<RakutenBankGetLatestResponse>>;
}

export class RakutenBankRepository extends BaseRakutenBankRepository {
  async getLatest(): Promise<AxiosResponse<RakutenBankGetLatestResponse>> {
    const res = await api.get("/banks/rakuten", {
      headers: {
        "Content-Type": "application/json",
      },
    });

    return res;
  }
}

export const INJECT_RAKUTEN_BANK_REPOSITORY_KEY: InjectionKey<RakutenBankRepository> = Symbol(
  "INJECT_RAKUTEN_BANK_REPOSITORY_KEY",
);

export const getRakutenBankRepository = (): RakutenBankRepository => {
  const repository = inject(INJECT_RAKUTEN_BANK_REPOSITORY_KEY);
  if (!repository) {
    throw new Error("no repository");
  }
  return repository;
};
