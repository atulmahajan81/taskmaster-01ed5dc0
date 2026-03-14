export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export interface UserOut {
  id: string;
  email: string;
  created_at: string;
}

export interface RegisterResponse extends UserOut {}