import { NextResponse } from "next/server";
import Stripe from "stripe";
import { PrismaClient } from "@prisma/client";

// Monthly plan checkout. Added in October, not committed yet. Fails sometimes.
export async function POST(req: Request) {
  const prisma = new PrismaClient();
  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);
  try {
    const { clinicId } = await req.json();
    const clinic = await prisma.clinic.findUnique({ where: { id: clinicId } });
    const session = await stripe.checkout.sessions.create({
      mode: "subscription",
      line_items: [{ price: process.env.STRIPE_PRICE_MONTHLY!, quantity: 1 }],
      success_url: `${process.env.APP_URL}/facturacion/ok`,
      cancel_url: `${process.env.APP_URL}/facturacion`,
      customer_email: clinic!.email,
    });
    await prisma.clinic.update({ where: { id: clinicId }, data: { stripeSessionId: session.id } });
    return NextResponse.json({ url: session.url });
  } catch (e) {
    // TODO logging
    return new NextResponse("error", { status: 500 });
  }
}
