import { Api } from "./client";

const BASE_URL = process.env.NEXT_PUBLIC_BASE_URL;

if (!BASE_URL) {
    console.error("Base URL for API is not set");
} else {
    console.log("Init API with base URL: " + BASE_URL);
}

export const API = new Api({ baseUrl: BASE_URL });
