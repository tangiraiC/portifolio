// Central configuration for API URLs
// In production, valid VITE_API_URL env var will be used.
// Locally it falls back to 127.0.0.1:8000

// Ensure no trailing slash for consistency
const getBaseUrl = () => {
    let url = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';
    if (url.endsWith('/')) {
        url = url.slice(0, -1);
    }
    return url;
}

const API_BASE_URL = getBaseUrl();
const API_URL = `${API_BASE_URL}/api`;

export default {
    API_BASE_URL,
    API_URL, // Export specific /api root
    // Endpoints
    BLOG: `${API_URL}/blog/`,
    PROJECTS: `${API_URL}/projects/`,
    PUBLICATIONS: `${API_URL}/research/`,
    RESUME: `${API_URL}/resume/`,
    CERTIFICATIONS: `${API_URL}/certifications/`,
    CONTACT: `${API_URL}/contact/`,
    LOGIN: `${API_URL}/login/`,
    REGISTER: `${API_URL}/register/`,
    PASSWORD_RESET: `${API_URL}/password-reset/`,
    PASSWORD_RESET_CONFIRM: `${API_URL}/password-reset/confirm/`,
}

