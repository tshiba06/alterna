import type { AxiosResponse } from "axios";
import api from "../services/api";

// Type definitions
type SbiShinseiBankGetLatestResponse = {
  total: number;
};

// Abstract class
export abstract class BaseSbiShinseiBankRepository {
  abstract getLatest(): Promise<AxiosResponse<SbiShinseiBankGetLatestResponse>>;
  abstract update(): Promise<AxiosResponse<undefined>>;
}

// Concrete class
export class SbiShinseiBankRepository extends BaseSbiShinseiBankRepository {
  async getLatest(): Promise<AxiosResponse<SbiShinseiBankGetLatestResponse>> {
    const res = await api.get("/banks/sbi_shinsei", {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res;
  }

  async update(): Promise<AxiosResponse<undefined>> {
    // The original repository sends an empty object as data for the POST request.
    const res = await api.post("/banks/sbi_shinsei", {}, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res;
  }
}

// Optional: Export an instance for singleton-like usage
export const sbiShinseiBankRepository = new SbiShinseiBankRepository();
