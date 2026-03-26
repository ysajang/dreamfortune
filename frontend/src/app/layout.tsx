// frontend/src/app/layout.tsx
import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "꿈해몽+운세 | 매일 아침 30초",
  description: "간밤에 꾼 꿈을 AI가 해몽해드려요. 오늘의 운세와 타로까지!",
  manifest: "/manifest.json",
  appleWebApp: {
    capable: true,
    statusBarStyle: "black-translucent",
    title: "꿈해몽",
  },
  openGraph: {
    title: "꿈해몽+운세 | 매일 아침 30초",
    description: "간밤에 꾼 꿈을 해몽받고 오늘의 운세까지 확인하세요",
    url: "https://dreamfortune.kr",
    siteName: "꿈해몽+운세",
    locale: "ko_KR",
    type: "website",
  },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  themeColor: "#1a0533",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ko">
      <head>
        <link rel="apple-touch-icon" href="/icons/icon-192x192.png" />
      </head>
      <body className="bg-[#0d1b2a] text-white min-h-screen">
        {children}
      </body>
    </html>
  );
}
