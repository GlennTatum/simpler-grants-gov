import { environment } from "src/constants/environments";
import { ApiMethod, HeadersDict, JSONRequestBody } from "src/services/fetch/fetcherHelpers";
import { requesterForEndpoint } from "src/services/fetch/fetchers/fetchers";
import { ApiRequestError, parseErrorStatus } from "src/errors";
import { EndpointConfig } from "src/services/fetch/endpointConfigs";
import { Counter } from "./count";


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

type EligibleDescriptionCollection = {
    data: EligibleDescription[]
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

    const eligible = await callEndpoint<EligibleDescriptionCollection>(eligibleEndpoint);


    return (
        <>
            {eligible.data.map((value) => {return <li key={value.description}>{value.description}</li>})}
            <Counter />
        </>
    );
}

const callEndpoint = async <ResponseCollection extends {data: unknown[]}>(endpoint: EndpointConfig, _subPath?: string, _body?: JSONRequestBody, _additionalHeaders?: HeadersDict) => {
    let res = {} as ResponseCollection
    try {
        const response = requesterForEndpoint(endpoint)
        const responseBody = ((await response({subPath: _subPath, body: _body, additionalHeaders: _additionalHeaders})).json()) as Promise<ResponseCollection>;
        res = (await responseBody)
    } catch (error) {
        console.error("Failed to render page title due to API error", error);
        if (parseErrorStatus(error as ApiRequestError) === 404) {
          throw error;
        }
    }
    return res

}