import utils
import streamlit as st
from streaming import StreamHandler
import PyPDF2    
from reportlab.pdfgen import canvas
import os
from fpdf import FPDF
from langchain.llms import OpenAI
from langchain.chains import ConversationChain

st.set_page_config(page_title="LegalEase: Generate with Ease", page_icon="⚖️")
st.header('LegalEase: Generate with Ease📃')
st.markdown("""
    Generate basic documents required by startups from below list with ease.
    """)
with st.expander("Implementation details"):
    st.markdown("""
    - LLM - [OpenAI](https://python.langchain.com/docs/ecosystem/integrations/openai#llm)
    - Chain - [ConversationChain](https://github.com/hwchase17/langchain/blob/1d649b127eb10c426f9b9a67cbd1fe6ec8e6befa/langchain/chains/conversation/base.py#L12)
    """)

def upload_new_template():
        file = st.file_uploader("Upload a PDF file", type=["pdf"])
        if file is not None:
            extract_text_from_pdf(file)
            st.success("File uploaded successfully!")

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
    text = '''
        State of <STATE>  
        NON -DISCLOSURE AND CONFIDENTIALITY AGREEMENT  
        This Non -Disclosure and Confidentiality Agreement (this “Agreement”) is entered into as of 
        <EFFECTIVE_DATE> (the “Effective Date”) by and between: 
        Disclosing Party: <DISCLOSING_PARTY> , as a(n) (Check one)   ☐   Individual 
        ☐Corporation  ☐   Limited Liability Company   ☐   Partnership   ☐   Limited Partnership   ☐   Limited
        Liability Partnership ("Disclosing Party") and
        Receiving Party:  <RECEIVING_PARTY> , as a(n) (Check one)   ☐   Individual 
        ☐Corporation  ☐   Limited Liability Company   ☐   Partnership   ☐   Limited Partnership   ☐   Limited
        Liability Partnership ("Receiving Party")
        Disclosing Party  and Receiving Party  have indicated an interest in exploring a potential business 
        relationship relating to: <TRANSACTION> (the “Transaction”).  
        In connection with its respective evaluation of the Transaction, each party, their respective affiliates and 
        their respective directors, officers, employees, agents or advisors (collectively, “Representatives”) may 
        provide or gain access to certain confidential and proprietary information. A party disclosing its Confidential Information to the other party is hereafter referred to as a “Disclosing Party.” A party receivi ng the Confidential Information of a Disclosing Party is hereafter referred to as a “Receiving Party.” 
        In consideration for being furnished Confidential Information, Disclosing Party  and Receiving Party  agree 
        as follows:  
        1.Confidential Information.  Confidential information is: (Check one)
        ☐Al
        l information shared by Disclosing Party.  "Confidential Information" shall mean (i) all informatio n
        relating to Disclosing Party’s products, business and operations including, but not limited to, financial
        documents and plans, customers, suppliers, manufacturing partners, marketing strategies, vendors,products, product development plans, technical product data, product samples, costs, sources, strategies,operations procedures, proprietary concepts, inventi ons, sales leads, sales data, customer lists, customer
        profiles, technical advice or knowledge, contractual agreements, price lists, supplier lists, sales estimates,product specifications, trade secrets, distribution methods, inventories, marketing strategies, source code,software, algorithms, data, drawings or schematics, blueprints, computer programs and systems an
        dknow-how or other intellectual property of Disclosing Party and its affiliates that may be at any tim e
        furnished, communicated or delivered by Disclosing Party to Receiving Party, whether in oral, tangible,
        electronic or other form; (ii) the terms of any agreement, including this Agreement, and the discussions,negotiations and proposals related to any agreement; (iii) information acquired during any tours ofDisclosing Party’s facilities; and (iv) all other non- public information provided by Disclosing Party
        whosoever. All Confidential Information shall remain the property of Disclosing Party.
        
        
        ☐   Only information marked ‘Confidential .’ "Confidential Information," exchanged by the parties and 
        entitled to protection hereunder, shall be identified or marked as such by an appropriate stamp or marking 
        on each document exchanged designating the information as confidential or proprietary.  
        
        ☐   Specific information.  The term “Confidential Information” as used in this Agreement shall mean any 
        data or information that is competitively sensitive material and not generally known to the public, 
        including, but not limited to, information relating to any of the following, which Disclosing Party considers 
        confidential:  (Check all that apply)  
        
        ☐   'Accounting Information' which includes all books, tax returns, financial information, financial 
        forecasts, pricing lists, purchasing lists and memos, pricing forecasts, purchase order information, supplier costs and discounts, or related financial or purchasing information.
        
        
        ☐   'Business Operations' which includes all processes, proprietary information or data, ideas or the 
        like, either in existence or contemplated related to Disclosing Party’s daily and long- term plans for 
        conducting Disclosing Party's business.  
        
        ☐   'Computer Technology' which includes all computer hardware, software or other tangible and 
        intangible equipment or code either in existence or development.  
        
        ☐   'Customer Information' which includes the names of entities or individuals, including their affiliates 
        and representatives, that Disclosing Party provides and sells its services or goods to, as well as any 
        associated information, including but not limited to, leads, contact lists, sales plans and notes, shared 
        and learned sales information such as pricing sheets, projections or plans, agreements, or such other data.  
        
        ☐   'Intellectual Property' which includes patents, trademarks,  service marks, logos, trade names, 
        internet or website domain names, rights in designs and schematics, copyrights (including rights in 
        computer software), moral rights, database rights, in each case whether registered or unregistered and including applications for registration, in all rights or forms anywhere in the world.  
        
        ☐   'Marketing and Sales Information' which includes all customer leads, sales targets, sales markets, 
        advertising materials, sales territories, sales goals and projections, sales and marketing processes or 
        practices, training manuals or other documentation and materials related to the sales, marketing and 
        promotional activities of the Disclosing Party and its products or services.  
        
        ☐   'Proprietary Rights’ which includes any and all  rights, whether registered or unregistered, in and 
        with respect to patents, copyrights, trade names, domain names, logos, trademarks, service marks, 
        confidential information, know -how, trade secrets, moral rights, contract or licensing rights, whether 
        protected under contract or otherwise under law, and other similar rights or interests in intellectual property.  
        
        
        ☐   'Procedures and Specifications' which includes all procedures and other specifications, criteria, 
        standards, methods, instructions, plans or other directions prescribed by Disclosing Party for the 
        manufacture, preparation, packaging and labelling, and sale of its products or services.  
        
        ☐   'Product Information' which includes Disclosing Party’s products which are being contemplated for 
        sale, manufactured, marketed, listed, or sold, including any fixes, revisions, upgrades, or versions, of 
        which consists of all data, software and documentation related thereto.  
        
        ☐   'Service Information' which means the services provided by Disclosing Party,  including the 
        method, details, means, skills and training, which consists of all data, software and documentation 
        related thereto.  
        
        ☐   'Software Information' which means the proprietary computer programs of Disclosing Party, 
        including all fixes, upgrades, new versions, new enhancements, modifications, edits, conversions, 
        replacements, or the like, in machine readable form or documentation and materials, and all copies 
        and translations of such computer programs, documentation and materials, regardless of  the form or 
        media of expression or storage.  
        
        ☐   Other:  ________________________________________________________________________  
        _________________________________________________________________________________
        _________________________________________________________________________________  
        
        2.  Exclusions from Confidential Information.  The obligation of confidentiality with respect  to 
        Confidential Information will not apply to any information:  
        
        a. If the information is or becomes publicly known and available other than as a result of prior unauthorized disclosure by Receiving Party or any of its Representatives;   
        b. If the informati on is or was received by Receiving Party from a third party source which, to the best 
        knowledge of Receiving Party or its Representatives, is or was not under a confidentiality obligation to 
        Disclosing Party with regard to such information;   
        c. If the info rmation is disclosed by Receiving Party with the Disclosing Party’s prior written permission 
        and approval;   
        d. If the information is independently developed by Receiving Party prior to disclosure by Disclosing 
        Party and without the use and benefit of any of the Disclosing Party’s Confidential Information; or  
        e. If Receiving Party or any of its Representatives is legally compelled by applicable law, by any court, governmental agency or regulatory authority or by subpoena or discovery request in pending litigation but only if, to the extent lawful, Receiving Party or its Representatives give prompt written notice of 
        that fact to Disclosing Party prior to disclosure so that Disclosing Party may request a protective order 
        or other remedy to prevent or limit such disclosure and in the absence of such protective order or 
        other remedy, Receiving Party or its Representatives may disclose only such portion of the Confidential Information which it is legally obligated to disclose.  
        
        
        
        3.  Obligation to Maintain Confide ntiality.  With respect to Confidential Information:  
        
        a. Receiving Party and its Representatives agree to retain the Confidential Information of the 
        Disclosing Party in strict confidence, to protect the security, integrity and confidentiality of such 
        inform ation and to not permit unauthorized access to or unauthorized use, disclosure, publication or 
        dissemination of Confidential Information except in conformity with this Agreement;   
        b. Receiving Party and its Representatives shall adopt and/or maintain secur ity processes and 
        procedures to safeguard the confidentiality of all Confidential Information received by Disclosing Party 
        using a reasonable degree of care, but not less than that degree of care used in safeguarding its own 
        similar information or material ; 
        c. Upon the termination of this Agreement, Receiving Party will ensure that all documents, 
        memoranda, notes and other writings or electronic records prepared by it that include or reflect any 
        Confidential Information are returned or destroyed as directed by Disclosing Party;  
        d. If there is an unauthorized disclosure or loss of any of the Confidential Information by Receiving Party or any of its Representatives, Receiving Party will promptly, at its own expense, notify Disclosing 
        Party in writing and take all actions as may be necessary or reasonably requested by Disclosing Party 
        to minimize any damage to the Disclosing Party or a third party as a result of the disclosure or loss; 
        and 
        e. The obligation not to disclose Confidential Information shall : (Check one) 
        
        ☐   Survive the termination of this Agreement, and at no time will Receiving Party or any of its 
        Representatives be permitted to disclose Confidential Information, except to the extent that such 
        Confidential Information is excluded from the obligations of confidentiality under this Agreement 
        pursuant to Paragraph 2 above.  
        ☐   Remain in effect until __________ (Check one)    ☐   months   ☐   years from the date hereof  or 
        until the Confidential Information ceases to be a trade secret , exce pt to the extent that such 
        Confidential Information is excluded from the obligations of confidentiality under this Agreement 
        pursuant to Paragraph 2 above.
        
        
        4.  Non- Disclosure of Transaction.  Without Disclosing Party’s prior written consent, neither Receiving 
        Party nor its Representatives shall disclose to any other person, except to the extent, the provisions of Paragraph 2 apply: (a) the fact that Confidential Information has been made available to it or that it has 
        inspected any portion of the Conf idential Information; (b) the fact that Disclosing Party and Receiving 
        Party are having discussions or negotiation concerning the Transaction; or (c) any of the terms, conditions or other facts with respect to the Transaction.  
        
        5.  Non- Compete.  (Cross out if you do not want to include a non -compete clause)  
        Receiving Party agrees that at no time will Receiving Party engage in any business activity which is 
        competitive with Disclosing Party, nor work for any company which competes with Disclosing party : 
        (Che ck one)  
        
        ☐   During the term of Receiving Party’s relationship with Disclosing Party . 
        ☐   From the date of this Agreement until ___________ ________ _, 20___ ___.
        
        
        
        6.  Non- Solicitation.  (Cross out if you do not want to include a non -solicitation  clause)  
        
        Receiving Party agrees not to solicit any employee or independent contractor of Disclosing Party on 
        behalf of any other business enterprise, nor shall Receiving Party induce any employee or independent 
        contractor associated with Disclosing Party to terminate or breach an employment, contractual or other 
        relationship with Disclosing Party : (Check one)  
        
        ☐   During the term of Receiving Party’s relationship with Disclosing Party . 
        ☐   From the date of this Agreement until ___________ ________ _, 20___ ___. 
        
        7.  Representatives.  Receiving Party will take reasonable steps to ensure that its Representatives 
        adhere to the terms of this Agreement. Receiving Party will be responsible for any breach of this 
        Agreement by any of its Representatives.  
        8.  Disclaimer.   There is no representation or warranty, express or implied, made by Disclosing Party as 
        to the accuracy or completeness of any of its Confidential Information. Except for the matters set forth in 
        this Agreement, neither party will be under any obligation w ith regard to the Transaction. Either party 
        may, in its sole discretion: (a) reject any proposals made by the other party or its Representatives with respect to the Transaction; (b) terminate discussions and negotiations with the other party or its 
        Represe ntatives at any time and for any reason or for no reason; and (c) change the procedures relating 
        to the consideration of the Transaction at any time without prior notice to the other party.  
        9.  Remedies.  Each party agrees that use or disclosure of any Con fidential Information in a manner 
        inconsistent with this Agreement will give rise to irreparable injury for which: (a) money damages may not be a sufficient remedy for any breach of this Agreement by such party; (b) the other party may be entitled 
        to speci fic performance and injunction and other equitable relief with respect to any such breach; (c) such 
        remedies will not be the exclusive remedies for any such breach, but will be in addition to all other remedies available at law or in equity; and (d) in the event of litigation relating to this Agreement, if a court 
        of competent jurisdiction determines in a final non- appealable order that one party, or any of its 
        Representatives, has breached this Agreement, such party will be liable for reasonable legal fees  and 
        expenses incurred by the other party in connection with such litigation, including, but not limited to, any 
        appeals.  
        
        10.  Notices.   All notices given under this Agreement must be in writing. A notice is effective upon receipt 
        and shall be sent via one of the following methods: delivery in person, overnight courier service, certified or registered mail, postage prepaid, return receipt requested, addressed to the party to be notified at the 
        below address or by facsimile at the below facsimile number or in the case of either party, to such other 
        party, address or facsimile number as such party may designate upon reasonable notice to the other party.  
        
        Disclosing Party  
        Name: ________________________  
        Representative name: ________________________ Title: ________________________  
        Address: ________________________________________  
        Phone number: ________________________  
        
        Fax number: ________________________  
        
        Receiving  Party  
        Name: ________________________  
        Representative name: ________________________ Title: ________________________  
        Address: ________________________________________  
        Phone number: ________________________  
        Fax number: ________________________  
        
        11.  Termination.  This Agreement will terminate on the earlier of:  
        
        (a) the written agreement of the par ties to terminate this Agreement;  
        (b) the consummation of the Transaction or  
        (c) __________ (Check one)   ☐   months   ☐   years from the date hereof.  
        
        12.  Amendment. This Agreement may be amended or modified only by a written agreement signed by 
        both of the parties.   
        
        13.  Jurisdiction.  This Agreement will be governed by and construed in accordance with the laws of the 
        State of _________________, without regard to the principles of conflict of laws. Each party consents to 
        the exclusive jurisdiction of the courts located in the State of _________________  for any legal action, 
        suit or proceeding arising out of or in connection with this Agreement. Each party further waiv es any 
        objection to the laying of venue for any such suit, action or proceeding in such courts.   
        
        14.  Miscellaneous.  This Agreement will inure to the benefit of and be binding on the respective 
        successors and permitted assigns of the parties. Neither part y may assign its rights or delegate its duties 
        under this Agreement without the other party’s prior written consent. In the event that any provision of this 
        Agreement is held to be invalid, illegal or unenforceable in whole or in part, the remaining provis ions shall 
        not be affected and shall continue to be valid, legal and enforceable as though the invalid, illegal or 
        unenforceable parts had not been included in this Agreement. Neither party will be charged with any 
        waiver of any provision of this Agreement , unless such waiver is evidenced by a writing signed by the 
        party and any such waiver will be limited to the terms of such writing.  
        IN WITNESS WHEREOF, the parties hereto have executed this Agreement as of the date first written 
        above.  
        
        
        Disclosing Party:  
        
        
        
        
        Disclosing Party  Signature   Disclosing Party  Full Name  
        
        
        
        
        
        Disclosing Party  Repre sentative  
        Signature   Disclosing Party  Representative  
        Full Name  and Title  
        
        
        Receiving Party:  
        
        
        
        
        Receiving  Party  Signature   Receiving  Party  Full Name  
        
        
        
        
        
        Receiving  Party  Repre sentative  
        Signature   Receiving  Party  Representative  
        Full Name  and Title  '''
    return text

def update_and_save_pdf(file_path, state, effective_date, disclosing_party, receiving_party, transaction):
    # Extract text from the original PDF file
    original_text = extract_text_from_pdf(file_path)
    # Update the extracted text
    updated_text = original_text.replace('<STATE>', state)
    updated_text = original_text.replace('<EFFECTIVE_DATE>', effective_date)
    updated_text = updated_text.replace('<DISCLOSING_PARTY>', disclosing_party)
    updated_text = updated_text.replace('<RECEIVING_PARTY>', receiving_party)
    updated_text = updated_text.replace('<TRANSACTION>', transaction)
    updated_text = updated_text.encode('latin-1', 'replace').decode('latin-1')

    # Create a new PDF file with the updated text
    new_file_path = file_path.replace('.pdf', '_updated.pdf')
    
    # Generate PDF from the updated text
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, updated_text)
    pdf.output(new_file_path, "F")

    return new_file_path



def work_with_existing_template(template):
    if template == "NDA":
        file_path = 'data/Non-Disclosure-Agreement-NDA-Template.pdf'
        state = st.text_input("Enter the state: ") 
        effective_date = st.text_input("Enter the effective date: ") 
        disclosing_party = st.text_input("Enter the disclosing party: ") 
        receiving_party = st.text_input("Enter the receiving party: ") 
        transaction = st.text_input("Enter the transaction: ")
        updated_file_path = update_and_save_pdf(file_path, state, effective_date, disclosing_party, receiving_party, transaction)
        st.success("Updated file saved at: " + updated_file_path)
class Basic:

    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"
    
    def setup_chain(self):
        llm = OpenAI(model_name=self.openai_model, temperature=0, streaming=True)
        chain = ConversationChain(llm=llm, verbose=True)
        return chain
        
    @utils.enable_chat_history
    def main(self):
        generation_option = st.radio("Select an option:", ("Upload new template", "Use existing template"))
        if generation_option == "Upload new template":
            upload_new_template()
        elif generation_option == "Use existing template":
            template = st.selectbox("Select a template:", ("NDA", "Master Agreement", "Evaluation Agreement"))
            work_with_existing_template(template)


if __name__ == "__main__":
    obj = Basic()
    obj.main()