import { environment } from "src/constants/environments";
import { ApiMethod } from "src/services/fetch/fetcherHelpers";
import { Counter } from "./count";
import { callEndpoint } from "./util";
import { generateAgencyNameLookup } from "src/utils/search/generateAgencyNameLookup";
import QuestionForm from "./Form";


// endpointConfigs.ts
const eligibleEndpoint = {
    basePath: environment.API_URL,
    version: "v1",
    namespace: "eligible_applicants",
    method: "POST" as ApiMethod,
}

type EligibleDescription = {
    description: string
}

export type EligibleDescriptionCollection = {
    data: EligibleDescription[]
}

type FundingInstrument = {
    title: string
}

export type FundingInstrumentCollection = {
    data: FundingInstrument[]
}

type Agency = {
    title: string
}

export type AgencyCollection = {
    data: Agency[]
}

type Category = {
    title: string
}

export type CategoryCollection = {
    data: Category[]
}

export default async function Questionnaire() {
    /**
     * Only query for Forecasted OR Posted Grants
     * 
     * User Story
     * 1. Grant Category (Optional default=None)
     *    Select the Grant Category 
     *    NOTE: (users should be advised that this may exclude them from
     *           grants they are looking to get)
     * 2. Grant Funding Requirements (Optional default=0)
     *     Show a slider of the Minimum Grant Floor
     * 3. Select your Institution/Agency (Eligibility)
     *    Display a checkbox stating if the user is an AGENCY of the United States Federal Government
     *      "I am apart of an agency of the federal government (1/0)"
     *       IF the user is apart of an agency create a search box where a
     *          user can select which agency they are apart of
     *    Otherwise
     *    Pick out of a list what your organization OR individual qualifies as
     *      - this should look like a list of buttons  side by side clumped where the
     *        user can easily check who they are
     * 3. 
     */

    // let EligibleData = {} as EligibleDescriptionCollection;

    // try {
    //     const response = requesterForEndpoint(eligibleEndpoint)
    //     const responseBody = ((await response()).json()) as Promise<EligibleAPIResponse>;
    //     EligibleData = (await responseBody)
    // } catch (error) {
    //     console.error("Failed to render page title due to API error", error);
    //     if (parseErrorStatus(error as ApiRequestError) === 404) {
    //       return notFound();
    // }
    // }

    const funding_instrument = {} as FundingInstrumentCollection;
    const eligible = await callEndpoint<EligibleDescriptionCollection>(eligibleEndpoint);
    const agency = {} as AgencyCollection;
    const category = {} as CategoryCollection;


    return (
        <>
            <QuestionForm 
                funding_instrument={funding_instrument}
                eligible={eligible}
                agency={agency}
                category={category}
            />
        </>
    );
}