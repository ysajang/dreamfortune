// frontend/src/sw.ts
import { defaultCache } from "@serwist/next/worker";
import type { PrecacheEntry, SerwistGlobalConfig } from "serwist";
import { Serwist } from "serwist";

declare global {
  interface WorkerGlobalScope extends SerwistGlobalConfig {
    __SW_MANIFEST: (PrecacheEntry | string)[] | undefined;
  }
}

declare const self: ServiceWorkerGlobalScope;

const serwist = new Serwist({
  precacheEntries: self.__SW_MANIFEST,
  skipWaiting: true,
  clientsClaim: true,
  navigationPreload: true,
  runtimeCaching: defaultCache,
});

// 푸시 알림 수신 핸들러
self.addEventListener("push", (event) => {
  const data = event.data?.json() ?? {};
  const title = data.title || "꿈해몽+운세";
  const options: NotificationOptions = {
    body: data.body || "오늘 아침 꿈을 기록해보세요 🌙",
    icon: "/icons/icon-192x192.png",
    badge: "/icons/badge-72x72.png",
    data: { url: data.url || "/" },
    tag: "dream-fortune",
  };
  event.waitUntil(self.registration.showNotification(title, options));
});

// 알림 클릭 핸들러
self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const url = event.notification.data?.url || "/";
  event.waitUntil(
    self.clients.matchAll({ type: "window" }).then((clients) => {
      for (const client of clients) {
        if (client.url === url && "focus" in client) return client.focus();
      }
      return self.clients.openWindow(url);
    })
  );
});

serwist.addEventListeners();
