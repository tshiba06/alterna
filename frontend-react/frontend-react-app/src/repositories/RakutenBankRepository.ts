import type { AxiosResponse } from "axios";
import api from "../services/api";

// Type definitions
type RakutenBankGetLatestResponse = {
  total: number;
};

// Abstract class
export abstract class BaseRakutenBankRepository {
  abstract getLatest(): Promise<AxiosResponse<RakutenBankGetLatestResponse>>;
  abstract update(): Promise<AxiosResponse<undefined>>;
}

// Concrete class
export class RakutenBankRepository extends BaseRakutenBankRepository {
  async getLatest(): Promise<AxiosResponse<RakutenBankGetLatestResponse>> {
    const res = await api.get("/banks/rakuten", {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res;
  }

  async update(): Promise<AxiosResponse<undefined>> {
    // The original repository sends an empty object as data for the POST request.
    // It's common for POST requests to have a body, even if empty.
    const res = await api.post("/banks/rakuten", {}, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res;
  }
}

// Optional: Export an instance for singleton-like usage
export const rakutenBankRepository = new RakutenBankRepository();
