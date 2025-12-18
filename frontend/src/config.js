// Central configuration for API URLs
// In production, valid VITE_API_URL env var will be used.
// Locally it falls back to 127.0.0.1:8000

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

export default {
    API_BASE_URL,
    // Endpoints
    BLOG: `${API_BASE_URL}/api/blog/`,
    PROJECTS: `${API_BASE_URL}/api/projects/`,
    PUBLICATIONS: `${API_BASE_URL}/api/research/`,
    RESUME: `${API_BASE_URL}/api/resume/`,
    CERTIFICATIONS: `${API_BASE_URL}/api/certifications/`,
    CONTACT: `${API_BASE_URL}/api/contact/`,
}
