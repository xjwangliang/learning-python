package com.taobao.api.request;

import java.util.Date;
import com.taobao.api.internal.util.RequestCheckUtils;
import java.util.Map;

import com.taobao.api.TaobaoRequest;
import com.taobao.api.internal.util.TaobaoHashMap;
import com.taobao.api.response.VmarketEticketOplogsGetResponse;
import com.taobao.api.ApiRuleException;
/**
 * TOP API: taobao.vmarket.eticket.oplogs.get request
 * 
 * @author auto create
 * @since 1.0, 2012-09-23 16:46:03
 */
public class VmarketEticketOplogsGetRequest implements TaobaoRequest<VmarketEticketOplogsGetResponse> {

	private TaobaoHashMap udfParams; // add user-defined text parameters
	private Long timestamp;

	/** 
	* 核销码
	 */
	private String code;

	/** 
	* 码商ID
	 */
	private Long codemerchantId;

	/** 
	* 结束时间
	 */
	private Date endTime;

	/** 
	* 手机号后四位
	 */
	private String mobile;

	/** 
	* 当前页码
	 */
	private Long pageNo;

	/** 
	* 每页显示的记录数，最大为40，默认为40
	 */
	private Long pageSize;

	/** 
	* 核销身份
	 */
	private String posid;

	/** 
	* 排序方式
	 */
	private String sort;

	/** 
	* 开始时间
	 */
	private Date startTime;

	/** 
	* 0:全部 1:核销 2:冲正
	 */
	private Long type;

	public void setCode(String code) {
		this.code = code;
	}
	public String getCode() {
		return this.code;
	}

	public void setCodemerchantId(Long codemerchantId) {
		this.codemerchantId = codemerchantId;
	}
	public Long getCodemerchantId() {
		return this.codemerchantId;
	}

	public void setEndTime(Date endTime) {
		this.endTime = endTime;
	}
	public Date getEndTime() {
		return this.endTime;
	}

	public void setMobile(String mobile) {
		this.mobile = mobile;
	}
	public String getMobile() {
		return this.mobile;
	}

	public void setPageNo(Long pageNo) {
		this.pageNo = pageNo;
	}
	public Long getPageNo() {
		return this.pageNo;
	}

	public void setPageSize(Long pageSize) {
		this.pageSize = pageSize;
	}
	public Long getPageSize() {
		return this.pageSize;
	}

	public void setPosid(String posid) {
		this.posid = posid;
	}
	public String getPosid() {
		return this.posid;
	}

	public void setSort(String sort) {
		this.sort = sort;
	}
	public String getSort() {
		return this.sort;
	}

	public void setStartTime(Date startTime) {
		this.startTime = startTime;
	}
	public Date getStartTime() {
		return this.startTime;
	}

	public void setType(Long type) {
		this.type = type;
	}
	public Long getType() {
		return this.type;
	}

	public Long getTimestamp() {
		return this.timestamp;
	}

	public void setTimestamp(Long timestamp) {
		this.timestamp = timestamp;
	}

	public String getApiMethodName() {
		return "taobao.vmarket.eticket.oplogs.get";
	}

	public Map<String, String> getTextParams() {		
		TaobaoHashMap txtParams = new TaobaoHashMap();
		txtParams.put("code", this.code);
		txtParams.put("codemerchant_id", this.codemerchantId);
		txtParams.put("end_time", this.endTime);
		txtParams.put("mobile", this.mobile);
		txtParams.put("page_no", this.pageNo);
		txtParams.put("page_size", this.pageSize);
		txtParams.put("posid", this.posid);
		txtParams.put("sort", this.sort);
		txtParams.put("start_time", this.startTime);
		txtParams.put("type", this.type);
		if(this.udfParams != null) {
			txtParams.putAll(this.udfParams);
		}
		return txtParams;
	}

	public void putOtherTextParam(String key, String value) {
		if(this.udfParams == null) {
			this.udfParams = new TaobaoHashMap();
		}
		this.udfParams.put(key, value);
	}

	public Class<VmarketEticketOplogsGetResponse> getResponseClass() {
		return VmarketEticketOplogsGetResponse.class;
	}

	public void check() throws ApiRuleException {
		
		RequestCheckUtils.checkNotEmpty(type,"type");
	}
}
