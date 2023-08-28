/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  eslint: {
    ignoreDuringBuilds: true,
  },
  images: {
    unoptimized: true,
  },
  async headers() {
    return [
        {
            source: '/(.*)?', // Matches all pages
            headers: [
                {
                    key: 'X-Frame-Options',
                    value: 'DENY',
                },{
                  key: 'Content-Security-Policy',
                  value:
                    "default-src 'self' 'https://dhruva.bhashini.gov.in'; image-src '*';",
                },
                {
                  key: 'X-Content-Type-Options',
                  value: 'nosniff',
                },
                {
                  key: 'Strict-Transport-Security',
                  value: 'max-age=3571000; includeSubDomains; preload',
                }
            ]
        }
    ]
}
};

module.exports = nextConfig;