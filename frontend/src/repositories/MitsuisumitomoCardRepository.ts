import type { AxiosResponse } from "axios";
import api from "../services/api";

const RESOURCE_PATH = "/cards/mitsuisumitomo";

// Type definitions
export type MitsuisumitomoCardGetLatestResponse = {
  total: number | null;
  message?: string;
};

export type MitsuisumitomoCardUpdateResponse = {
  message: string;
};

// Abstract class (optional, but good for consistency if other repositories use it)
export abstract class BaseMitsuisumitomoCardRepository {
  abstract update(): Promise<AxiosResponse<MitsuisumitomoCardUpdateResponse>>;
  abstract getLatest(): Promise<AxiosResponse<MitsuisumitomoCardGetLatestResponse>>;
}

// Concrete class
export class MitsuisumitomoCardRepository extends BaseMitsuisumitomoCardRepository {
  async update(): Promise<AxiosResponse<MitsuisumitomoCardUpdateResponse>> {
    const res = await api.post<MitsuisumitomoCardUpdateResponse>(`${RESOURCE_PATH}/save`);
    return res;
  }

  async getLatest(): Promise<AxiosResponse<MitsuisumitomoCardGetLatestResponse>> {
    const res = await api.get<MitsuisumitomoCardGetLatestResponse>(`${RESOURCE_PATH}/latest`);
    return res;
  }
}

// Optional: Export an instance for singleton-like usage
export const mitsuisumitomoCardRepository = new MitsuisumitomoCardRepository();
