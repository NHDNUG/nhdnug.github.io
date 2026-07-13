---
date:               "2026-09-17 17:30:00"
speakers:           ["Aaron Stannard"]
title:              "You Should Probably Be Using IAsyncEnumerable"
location:           "Beach Walk Coworking"
sponsors:           ["Petabridge"]
description:        "Task can't tell you whether a long-running job is alive or stuck. A better primitive for modeling background jobs, intermittent jobs, and producer-consumer relationships."
meetup:             "315672505"
survey-url:         ""
---

A job has been running for twenty minutes. Is it working, or is it dead?

You can't tell. Not from the outside.

`Task<T>` has three states: pending, completed, faulted. "Alive and making progress" and "stuck forever and never coming back" are the same one. That isn't an observability gap you can instrument your way out of. It's how Task is designed.

What we need is a better primitive for modeling longer running background jobs, intermittent jobs, and producer-consumer relationships. Enter `IAsyncEnumerable`, which allows us to model these tasks as asynchronous *streaming* jobs.

`IAsyncEnumerable<T>` isn't a sequence you await. It's a producer / consumer contract - you know it's alive when new events arrive during the *progression* of the job, rather than at its completion.

In this talk we'll look at several examples of .NET code where `IAsyncEnumerable` is crucial to ensure the success of the application:

- AI agent that runs two timers over its own token stream, so it can distinguish "nothing arrived, it's dead" scenarios from "heartbeats arriving, zero real output, it's alive and stuck."
- A 20-minute re-embedding job that streams progress over ASP.NET Core SSE, where a late subscriber's first element is the current state.
- And an e-commerce checkout page that used to poll for proof of fulfillment / payment activity, that now instead waits for events via SSE to drive navigation and behavior from the back-end.

You'll learn how and where to apply `IAsyncEnumerable` to solve your problems.

## Food / Drinks
Food and drinks will be provided! Please contact us (on meetup) if you have any dietary restrictions/food allergies.

## Directions and Parking Instructions

Meeting will be held at Beach Walk Coworking, 96 Beach Walk Blvd, Conroe, TX 77304 in the ground floor meeting room. Free parking is available on site.
