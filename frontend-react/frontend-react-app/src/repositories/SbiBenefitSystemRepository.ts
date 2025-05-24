import type { AxiosResponse } from "axios";
import api from "../services/api";

// Type definitions
type SbiBenefitSystemGetLatestResponse = {
  total: number;
};

// Abstract class
export abstract class BaseSbiBenefitSystemRepository {
  abstract getLatest(): Promise<AxiosResponse<SbiBenefitSystemGetLatestResponse>>;
  abstract update(): Promise<AxiosResponse<undefined>>;
}

// Concrete class
export class SbiBenefitSystemRepository extends BaseSbiBenefitSystemRepository {
  async getLatest(): Promise<AxiosResponse<SbiBenefitSystemGetLatestResponse>> {
    const res = await api.get("/pensions/sbi_benefit_system", {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res;
  }

  async update(): Promise<AxiosResponse<undefined>> {
    // The original repository sends an empty object as data for the POST request.
    const res = await api.post("/pensions/sbi_benefit_system", {}, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res;
  }
}

// Optional: Export an instance for singleton-like usage
export const sbiBenefitSystemRepository = new SbiBenefitSystemRepository();
