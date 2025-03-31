"use client";

import { JSX } from "react";
import { FormProgressState } from "./Form";

type FormContainerProps = {
    progress: FormProgressState
    elements: JSX.Element[]
}

export const FormContainer = ({
    progress,
    elements
}: FormContainerProps) => {

    return (
        <>
            <div className="bg-primary-darker height-viewport padding-8">
                <div className="grid-container">
                    <h1 className="text-white">Answer the following questions</h1>
                    <div className="bg-white radius-lg padding-4">
                        <div className="usa-step-indicator">
                            <ol className="usa-step-indicator__segments">
                                {elements.map((v, i) => {
                                    // swap >= -> >
                                    let isComplete = "usa-step-indicator__segment usa-step-indicator__segment"
                                    if(progress.current > i){isComplete = "usa-step-indicator__segment usa-step-indicator__segment--complete"}
                                    if(progress.current === i){ isComplete = "usa-step-indicator__segment usa-step-indicator__segment--current" }

                                    return (
                                        <li
                                        key={Math.random()}
                                        className={isComplete}
                                        >
                                        <span className="usa-step-indicator__segment-label"
                                        >{v.key}</span>
                                        </li>
                                    )
                                })}
                            </ol>
                        </div>
                        {elements.at(progress.current)}
                    </div>
                </div>
            </div>
        </>
    )
}