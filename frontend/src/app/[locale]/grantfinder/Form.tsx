"use client";

import { ChangeEvent, JSX, useRef, useState } from "react";
import { AgencyCollection, CategoryCollection, EligibleDescriptionCollection, FundingInstrumentCollection } from "./page"
import { GrantHelperInformation } from "./Information";
import { FormContainer } from "./FormContainer";
import { has, set } from "lodash";
import { Checkbox } from "@trussworks/react-uswds";
import FilterCheckbox from "src/components/FilterCheckbox";


type QuestionFormProps = {
    funding_instrument: FundingInstrumentCollection;
    eligible: EligibleDescriptionCollection;
    agency: AgencyCollection;
    category: CategoryCollection;
}

export type FormProgressHanldeProp = {
    progressHandle: (key: string, back: boolean) => void
}

export type FormStepProp = {
    stepIndicator: (name: string, complete: boolean) => JSX.Element
}

export type FormProgressState = {
    current: number,
}

export default function QuestionForm({
    funding_instrument,
    eligible,
    agency,
    category
}: QuestionFormProps) {


    const [getProgress, setProgress] = useState<FormProgressState>({
        current: -1,
    });

    const setProgressionState = (key: string, increment: boolean) => {
        if(increment) {
            setProgress({
                current: getProgress.current+1,
            })
        } else {
            setProgress({
                current: getProgress.current-1,
            })
        }
    }

    const QAbout = ({progressHandle}: FormProgressHanldeProp) => {
        const key = "About"

        const [isChecked, setChecked] = useState(false)

        const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
            const checked = event.target.checked;
            setChecked(checked)
          };

        const showUIDInfo = () => {
            if(isChecked) {
                return (
                    <>
                        <div>
                            <p>Congratulations! You are eligible to apply for grants!</p>
                        </div>
                    </>
                )
            }
            return (
                <>
                    <div>
                        <p>For for information on becoming eligible for grants go to <a target="_blank" rel="noopener noreferrer" href="https://sam.gov/entity-registration">SAM.gov</a></p>
                        <p><b>Note: </b>To apply to grants a UID is <b>required</b></p>
                    </div>
                </>
            )
        }

        return (
            <>
                <h1>{key}</h1>

                <Checkbox 
                id="checkbox" 
                name="checkbox" 
                label="I have registered a government Unique Entity ID" 
                onChange={handleChange}
                />
                {showUIDInfo()}
                <button className="usa-button margin-top-2" onClick={() => progressHandle(key, false)}>Back</button>
                <button className="usa-button margin-top-2" onClick={() => progressHandle(key, true)}>Next</button>
            </>
        )
    }

    const QEligible = ({progressHandle}: FormProgressHanldeProp) => {
        const key = "Eligible"


        // FIXME turn show select into own component
        const ShowSelect = eligible.data.map((item, i) => {
                const str = item.description.replaceAll("_", " ")
                return (
                    <span key={item.description + i.toString()}>
                        <FilterCheckbox 
                            id={item.description + i.toString()}
                            label={str}
                            onChange={() => ""}
                        />
                    </span>
                )
            })

        return (
            <>
                <h1>{key}</h1>
                <p>Choose the category your organization or indiviudal falls under</p>
                {ShowSelect}
                <button className="usa-button margin-top-2" onClick={() => progressHandle(key, false)}>Back</button>
                <button className="usa-button margin-top-2" onClick={() => progressHandle(key, true)}>Next</button>
            </>
        )
    }

    const QAgency = ({progressHandle}: FormProgressHanldeProp) => {
        const key = "Agency"

        return (
            <>
                <h1>{key}</h1>
                <button className="usa-button margin-top-2" onClick={() => progressHandle(key, false)}>Back</button>
                <button className="usa-button margin-top-2" onClick={() => progressHandle(key, true)}>Next</button>
            </>
        )
    }

    const RenderProgressState = () => {
        if(getProgress.current === -1) {
            return (
                <GrantHelperInformation  key={"GrantHelper"} progressHandle={setProgressionState}/>
            )
        }
        const formItems: JSX.Element[] = [
            <QAbout key={"About"} progressHandle={setProgressionState}></QAbout>,
            <QEligible key={"Eligible"} progressHandle={setProgressionState}></QEligible>,
            <QAgency key={"Agency"} progressHandle={setProgressionState}></QAgency>
        ]
        return (
            <FormContainer 
            progress={getProgress}
            elements={formItems}
            ></FormContainer>
        )
    }

    return (
        <>
            <RenderProgressState />
        </>
    )
}