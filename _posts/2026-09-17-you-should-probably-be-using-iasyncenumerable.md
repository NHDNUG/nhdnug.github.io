---
date:               "2026-09-17 17:30:00"
speakers:           ["Aaron Stannard"]
title:              "You Should Probably Be Using IAsyncEnumerable"
location:           "Beach Walk Coworking"
sponsors:           ["Petabridge"]
description:        "Task tells you a job is pending -- not whether it's alive. Why long-running work belongs in a stream, with three pieces of production code and the point where the thesis breaks."
meetup:             "315672505"
survey-url:         ""
---

A job has been running for twenty minutes. Is it working, or is it dead?

You can't tell. Not from the outside. `Task<T>` has three states: pending, completed, faulted. "Alive and making progress" and "wedged forever and never coming back" are the same one. That isn't an observability gap you can instrument your way out of. It's the return type.

Every timeout you've ever wrapped around a long-running call is a confession of this. You guessed a number, because the Task won't say anything until it's over.

`IAsyncEnumerable<T>` isn't a sequence you await. It's a producer / consumer contract, and a thing that unfolds over time can tell you it's still unfolding. An element arriving is proof of life.

You may already be writing this without having decided to. `TypedResults.ServerSentEvents` takes an `IAsyncEnumerable<SseItem<T>>`.

Three pieces of Petabridge production code, all public. An AI agent that runs two timers over its own token stream, so it can tell "nothing arrived, it's dead" from "heartbeats arriving, zero real output, it's alive and stuck." A 20-minute re-embedding job that streams progress over SSE, where a late subscriber's first element is the current state. And a checkout that polled every 200ms, 3,738ms cold, until it stopped polling and started subscribing.

Then I'll break my own thesis. `IAsyncEnumerable` backpressures the consumer and barely touches the producer. Channels do it weakly, and I'll show you my own code hand-rolling a 500ms throttle to hide that. Some producers can't be slowed at all: the Claude API streaming tokens at you, Kafka, the physical world. Then your only honest move is an explicit lossy policy.

You'll leave knowing which Tasks in your codebase should have been streams.

## Food / Drinks
Food and drinks will be provided! Please contact us (on meetup) if you have any dietary restrictions/food allergies.

## Directions and Parking Instructions

Meeting will be held at Beach Walk Coworking, 96 Beach Walk Blvd, Conroe, TX 77304 in the ground floor meeting room. Free parking is available on site.
