import type { AxiosResponse } from "axios";
import api from "../services/api";

// Type definitions
type SumishinSbiBankGetLatestResponse = {
  total: number;
};

// Abstract class
export abstract class BaseSumishinSbiBankRepository {
  abstract getLatest(): Promise<AxiosResponse<SumishinSbiBankGetLatestResponse>>;
  abstract update(): Promise<AxiosResponse<undefined>>;
}

// Concrete class
export class SumishinSbiBankRepository extends BaseSumishinSbiBankRepository {
  async getLatest(): Promise<AxiosResponse<SumishinSbiBankGetLatestResponse>> {
    const res = await api.get("/banks/sumishin_sbi", {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res;
  }

  async update(): Promise<AxiosResponse<undefined>> {
    // The original repository sends an empty object as data for the POST request.
    const res = await api.post("/banks/sumishin_sbi", {}, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res;
  }
}

// Optional: Export an instance for singleton-like usage
export const sumishinSbiBankRepository = new SumishinSbiBankRepository();
