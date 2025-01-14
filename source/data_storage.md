# Data Storage
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/e89f5ef3a5fe530fda28f196c8ab88cbcf5586b3/source/data_storage.md" class="reference">15 Feb 2022</a>

Whether you're using the humanitarian server supported by
[UNOCHA](https://kobo.humanitarianresponse.info/accounts/login/?next=/#/) or the
non-humanitarian server supported by
[Kobo, Inc.](https://kf.kobotoolbox.org/accounts/login/?next=/#/), the data from
both servers is stored on Amazon Web Services (AWS) servers.

There are 2 kinds of data stored on AWS, the form itself and the attachments
related to each submission. The data of the form is saved into the Database (DB)
and the attachments are saved into Simple Storage Service (S3). The stored data
in the Database is never deleted unless you delete the data yourself. The
collected data on S3 is also never deleted, unless you delete it yourself or you
end up using more space then you're allowed according to the
[OCHA/Kobo policies](server.md).

You can keep up to 10 data exports at a time per project. If you create an 11th
export, the oldest one is deleted and only the 10 most recent exports are kept.

For more information on KoboToolbox data security measures, please refer to this
other [help article](is_my_data_safe.md).
