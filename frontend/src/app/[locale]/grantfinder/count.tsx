"use client";

import { useState } from "react";

export const Counter = () => {
    const [getCount, setCount] = useState(0);

    return (
        <button onClick={() => setCount(getCount + 1)}>{getCount}</button>
    )
}