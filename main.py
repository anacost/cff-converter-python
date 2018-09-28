# Entry file for google cloud functions

from cffconvert import Citation
from flask import Response

def convert(request):
    try:
        url = request.args.get('url')
        outputformat = request.args.get('format')

        if url:
            citation = Citation(url=url, validate=True)
        else:
            citation = Citation(cffstr=request.data.decode('utf-8'), validate=True)

        if outputformat == "bibtex":
            outstr = citation.as_bibtex()
        elif outputformat == "codemeta":
            outstr = citation.as_codemeta()
        elif outputformat == "endnote":
            outstr = citation.as_enw()
        elif outputformat == "ris":
            outstr = citation.as_ris()
        elif outputformat == "zenodo":
            outstr = citation.as_zenodojson()
        elif outputformat == "cff":
            outstr = citation.cffstr
        else:
            raise Exception('unknown output format: %s' % outputformat)

        return Response(outstr, mimetype='text/plain')

    except Exception as e:
        return Response(str(e), mimetype='text/plain', status=400)
