---
id: assert
title: Assert
sidebar_label: Assert
---

<pre><code>
asserts:
  - type: <a href="#type">string</a> (required)
    name: <a href="#name">string</a>
    template: <a href="#template">string</a>
    storeVersions: <a href="#store-versions">bool</a>
    params: <a href="#params">Map</a>
    keepIfPassed: <a href="#keep-if-passed">bool</a>
    passed: <a href="#passed">bool</a>
    actual: <a href="#actual">string</a>
    expected: <a href="#expected">string</a>
    description: <a href="#description">string</a>
</code></pre>

## Assert Params

### Type

`REQUIRED` Type of assert (See runner's supported assert types)

> ### NullAssert
> If `type` is set to `NullAssert`, the assert results will be populated with
> the provided values for <a href="#passed">`passed`</a>, <a href="#actual">`actual`</a>,
> <a href="#expected">`expected`</a>, and <a href="#description">`description`</a>

### Name

Name of assert. If not specified, it will be inferred from the runner's type.

### Template

Template string to be rendered into assert using the state container

### Store Versions

Store all results of an assert in the state container. If `false`, will overwrite
the last result and store assert results as a single value instead of a list.

Defaults to `true`

### Params

Parameters to provide to assert (See runner's supported action params)

### Keep if Passed

Test will continue running with this assert even if it has passed if set to `false`.

Defaults to `true`

### Actual

Sets assert result's `actual` value to the one provided is using a <a href="#nullassert">`NullAssert`</a>

### Expected

Sets assert result's `expected` value to the one provided is using a <a href="#nullassert">`NullAssert`</a>

### Passed

Sets assert result's `passed` value to the one provided is using a <a href="#nullassert">`NullAssert`</a>

### Description

Sets assert result's `description` value to the one provided is using a <a href="#nullassert">`NullAssert`</a>
