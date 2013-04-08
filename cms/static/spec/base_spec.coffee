describe "#editSectionPublishDate", ->
    beforeEach ->
       jasmine.getFixtures().fixturesPath = "fixtures/"
       loadFixtures 'edit-subsection-publish-settings.html'
       $('body').addClass("course").addClass("outline")

    afterEach ->
        hideModal()
        $('body').removeClass("course").removeClass("outline")

    it "clicking the edit button should show the date edit modal", ->
        $s = $('.edit-subsection-publish-settings')
        expect($s).toBeHidden()
        fakeEvent = {
            preventDefault: ->
        }
        editSectionPublishDate(fakeEvent)
        expect($s).not.toBeHidden()
