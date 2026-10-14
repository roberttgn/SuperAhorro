import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "SuperAhorro | Compara tu cesta", description: "Compara el coste de tu compra. Prototipo con precios ficticios identificados." };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="es"><body>{children}</body></html>; }