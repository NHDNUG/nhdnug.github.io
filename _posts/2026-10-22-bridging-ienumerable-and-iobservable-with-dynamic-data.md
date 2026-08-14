---
date:               "2026-10-22 17:30:00"
speakers:           ["Rodney Littles, II"]
title:              "Bridging IEnumerable and IObservable with Dynamic Data"
location:           "Beach Walk Coworking"
sponsors:           ["Petabridge"]
description:        "Dynamic Data bridges IEnumerable and IObservable, giving you reactive operators — Filter, Transform, Sort, AutoRefresh, Batch — that pipe collection changes straight to the UI."
meetup:             "316119800"
survey-url:         ""
---

You've bound a list, updated an item's property, and watched the UI do nothing. That gap in `ObservableCollection<T>` is by design: binding a list requires `INotifyCollectionChanged` — not just `INotifyPropertyChanged` — and out of the box the two don't compose. Dynamic Data, created by Roland Pheasant and now a dependency of ReactiveUI, bridges `IEnumerable` and `IObservable` by projecting change sets out of your collections. With a `SourceCache<T, TKey>` or `SourceList<T>` at the core, you get reactive operators — Filter, Transform, Sort, AutoRefresh, Batch — that can be driven by other observables. Want the list to re-sort every time a picker selection changes? That's one operator. Want property changes inside list items to trigger a new sort pass? That's one operator. In this session we'll demonstrate a few working view models that connect to a data source and pipe changes all the way to the UI — without a single `foreach`, event handler, or manual `ObservableCollection` reassignment.

*Difficulty: Intermediate — helpful to know C#, MVVM, and Reactive Extensions basics going in.*

## Food / Drinks
Food and drinks will be provided! Please contact us (on meetup) if you have any dietary restrictions/food allergies.

## Directions and Parking Instructions

Meeting will be held at Beach Walk Coworking, 96 Beach Walk Blvd, Conroe, TX 77304 in the ground floor meeting room. Free parking is available on site.
