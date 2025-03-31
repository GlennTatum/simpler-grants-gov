import { FormProgressHanldeProp } from "./Form"

export const GrantHelperInformation = ({progressHandle}: FormProgressHanldeProp) => {
    return (
        <>
            <div className="bg-primary-darker height-card padding-4">
                <div className="grid-container-tablet-lg">
                    <div className="font-sans-xl text-white">
                        <b>Grant Finder: all grants</b>
                    </div>
                    <p className="text-white">
                        <b>Find public grant information. Start here to search for grants</b>
                    </p>
                </div>
            </div>
            <div className="grid-container-tablet-lg margin-top-5">
                <div className="grid-container">
                    <div className="font-sans-xl margin-bottom-2">Steps to find grants</div>
                    <ol className="usa-process-list font-sans-xl">
                        <li className="usa-process-list__item padding-bottom-10">
                            <p className="usa-process-list__heading line-height-sans-1">
                            Answer a few questions
                            </p>
                        </li>
                        <li className="usa-process-list__item padding-bottom-10">
                            <p className="usa-process-list__heading line-height-sans-1">
                            Get your list of grants
                            </p>
                        </li>
                        <li className="usa-process-list__item">
                            <p className="usa-process-list__heading line-height-sans-1">
                            Contact grantmakers to apply
                            </p>
                        </li>
                    </ol>
                    <hr></hr>
                    <div className="font-sans-xl margin-bottom-2">Before you start</div>
                    <p className="font-sans-4"><b>This is not an application. You will need to apply for grants</b> with each agency.</p>
                    <p><b>We do not share, save, or submit your information.</b></p>
                    <button className="usa-button margin-top-2" onClick={() => progressHandle("GrantHelper", true)}>Start finding grants</button>
                </div> 
            </div>
        </>
    )
}