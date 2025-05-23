import type { AxiosResponse } from "axios";
import { api } from "boot/axios"; // Assuming Quasar's boot file for axios

// Define response types if you have them, e.g.:
// interface SaveResponse { message: string; }
// interface LatestResponse { total: number | null; message?: string; }

const RESOURCE_PATH = "/cards/mitsuisumitomo";

export interface MitsuisumitomoCardRepository {
  update: () => Promise<AxiosResponse<{ message: string }>>; // POST /save
  getLatest: () => Promise<AxiosResponse<{ total: number | null; message?: string }>>;
}

const repository: MitsuisumitomoCardRepository = {
  update: () => {
    return api.post(`${RESOURCE_PATH}/save`);
  },
  getLatest: () => {
    return api.get(`${RESOURCE_PATH}/latest`);
  },
};

export const getMitsuisumitomoCardRepository = () => repository;
